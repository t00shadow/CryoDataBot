# original posted by kiharalab on https://github.com/kiharalab/CryoREAD/tree/main
# modified by Qibo Xu

import math

import mrcfile
import numpy as np

# from ops.acc_mean_shift import carry_shift, carry_shift_limit


class MRC(object):

    def __init__(self, file_name, gaussian_bandwidth=3.0, contour=0):
        """
        :param file_name: #File name of the mrc file
        :param params: parameter config
        """
        self.file_name = file_name
        self.gaussian_bandwidth = gaussian_bandwidth
        self.read_mrc(self.file_name, contour)
        # self.print_info()

    def read_mrc(self, file_name=None, contour=0):
        if file_name is not None:
            self.filename = file_name
        with mrcfile.open(self.file_name, permissive=True) as mrc:
            # Record header information from mrc file
            # number of sections/rows/columns in 3 dimensions
            self.nz, self.ny, self.nx = mrc.header.nz, mrc.header.ny, mrc.header.nx
            # the recording mode in the mrc file
            self.mode = mrc.header.mode
            """
            array (slow axis)
            location:13-16	MODE
                                0 8-bit signed integer (range -128 to 127)
                                1 16-bit signed integer
                                2 32-bit signed real
                                3 transform : complex 16-bit integers
                                4 transform : complex 32-bit reals
                                6 16-bit unsigned integer
            """
            # location of first section/row/column in unit cell
            self.nzstart = mrc.header.nzstart
            self.nystart = mrc.header.nystart
            self.nxstart = mrc.header.nxstart
            # sampling along Z,Y,X axis of unit cell
            self.mz, self.my, self.mx = mrc.header.mz, mrc.header.my, mrc.header.mx
            # cell dimensions in angstroms
            self.zlen = mrc.header.cella.z
            self.ylen = mrc.header.cella.y
            self.xlen = mrc.header.cella.x
            # cell angles in degrees
            self.alpha = mrc.header.cellb.alpha
            self.beta = mrc.header.cellb.beta
            self.gamma = mrc.header.cellb.gamma
            # axis corresponds to section/row/column, 1 represents X axis,2 is Y, 3 is Z
            self.maps = mrc.header.maps
            self.mapr = mrc.header.mapr
            self.mapc = mrc.header.mapc
            # minimum/maximum/density density value
            self.dmin = mrc.header.dmin
            self.dmax = mrc.header.dmax
            self.dmean = mrc.header.dmean
            # space group number
            self.ispg = mrc.header.ispg
            """explanation for ispg:
                Spacegroup 0 implies a 2D image or image stack.
                For crystallography, ISPG represents the actual spacegroup.
                For single volumes from EM/ET, the spacegroup should be 1.
                For volume stacks, we adopt the convention that ISPG is the spacegroup
            number + 400, which in EM/ET will typically be 401.
            """
            # NSYMBT
            self.nsymbt = mrc.header.nsymbt
            """NSYMBT specifies the size of the extended header in bytes,
            whether it contains symmetry records (as in the original format definition)
            or any other kind of additional metadata."""
            # ORIGIN
            self.originz = mrc.header.origin.z
            self.originy = mrc.header.origin.y
            self.originx = mrc.header.origin.x
            """
            Generally (not transforms), ORIGIN specifies the real space location of
                a subvolume taken from a larger volume. In the (2-dimensional) example
                shown above, the header of the map containing the subvolume (red
                rectangle) would contain ORIGIN = 100, 120 to specify its position with
                respect to the original volume (assuming the original volume has its
                own ORIGIN set to 0, 0).
            For transforms (Mode 3 or 4), ORIGIN is the phase origin of the transformed
                image in pixels, e.g. as used in helical processing of the MRC package.
            For a transform of a padded image, this value corresponds to the pixel
                position in the padded image of the center of the unpadded image.
            """

            # Record density data in the mrc file
            self.dens = np.array(mrc.data)
            # self.dens.flags.writeable=True
            self.shape = self.dens.shape
            self.NumVoxels = self.nz * self.ny * self.nx
            # length of each sampling on different axis
            self.widthz = self.zlen / self.mz
            self.widthy = self.ylen / self.my
            self.widthx = self.xlen / self.mx
            # axis order of the density data saved in mrc file
            self.ordermode = 0
            if self.mapc == 1 and self.mapr == 2 and self.maps == 3:
                self.ordermode = 1
                self.xdim = self.nx
                self.ydim = self.ny
                self.zdim = self.nz
            if self.mapc == 1 and self.mapr == 3 and self.maps == 2:
                self.ordermode = 2
                self.xdim = self.nx
                self.ydim = self.nz
                self.zdim = self.ny
            if self.mapc == 2 and self.mapr == 1 and self.maps == 3:
                self.ordermode = 3
                self.xdim = self.ny
                self.ydim = self.nx
                self.zdim = self.nz
            if self.mapc == 2 and self.mapr == 3 and self.maps == 1:
                self.ordermode = 4
                self.xdim = self.nz
                self.ydim = self.nx
                self.zdim = self.ny
            if self.mapc == 3 and self.mapr == 1 and self.maps == 2:
                self.ordermode = 5
                self.xdim = self.ny
                self.ydim = self.nz
                self.zdim = self.nx
            if self.mapc == 3 and self.mapr == 2 and self.maps == 1:
                self.ordermode = 6
                self.xdim = self.nz
                self.ydim = self.ny
                self.zdim = self.nx
        # retain only densities > 0
        self.dens[self.dens < contour] = 0
        return True

    def print_info(self):
        """
        Print all the information you get from the mrc file
        """
        print('information of ' + str(self.filename))
        print('The recording mode in the mrc file:' + str(self.mode))
        print("XYZ dim:%d,%d,%d" % (self.nx, self.ny, self.nz))
        print("location of first column/row/section in unit cell:%d,%d,%d" %
              (self.nxstart, self.nystart, self.nzstart))
        print("sampling along X,Y,Z axis of unit cell:%d,%d,%d" %
              (self.mx, self.my, self.mz))
        print('cell dimensions in angstroms:%f,%f,%f' %
              (self.xlen, self.ylen, self.zlen))
        print("Cell angles in degree:%d,%d,%d" %
              (self.alpha, self.beta, self.gamma))
        print("axis mode:(%d,%d,%d)" % (self.mapc, self.mapr, self.maps))
        print("density statistics:min(%f),max(%f),mean(%f)" %
              (self.dmin, self.dmax, self.dmean))
        print("space group number:%d " % self.ispg)
        print("extended data:%d " % self.nsymbt)
        print("origin state:(%f,%f,%f)" %
              (self.originx, self.originy, self.originz))
        print("density data shape:")
        print(self.dens.shape)
        print('min density:%f' % np.min(self.dens))
        print('max density:%f' % np.max(self.dens))
        print("number of voxels: " + str(self.NumVoxels))
        print("width of x,y,z:(%f,%f,%f)" %
              (self.widthx, self.widthy, self.widthz))
        print("order mode:%d" % (self.ordermode))

    def swap_back_coordinates(self, data, ordermode):
        # swap coordinates to make that of the density data [z, y, x]
        if ordermode == 1:
            map_data = data
            print('ordermode 1 no operation')
        elif ordermode == 2:
            map_data = data.swapaxes(1, 2)
            # data[:, [1, 2]] = data[:, [2, 1]]
        elif ordermode == 3:
            map_data = data.swapaxes(0, 1)
            # data[:, [0, 1]] = data[:, [1, 0]]
        elif ordermode == 4:
            map_data = data.swapaxes(1, 2)
            map_data = data.swapaxes(0, 1)
            # data[:, [1, 2]] = data[:, [2, 1]]
            # data[:, [0, 1]] = data[:, [1, 0]]
        elif ordermode == 5:
            map_data = data.swapaxes(0, 1)
            map_data = data.swapaxes(1, 2)
            # data[:, [0, 1]] = data[:, [1, 0]]
            # data[:, [1, 2]] = data[:, [2, 1]]
        elif ordermode == 6:
            map_data = data.swapaxes(0, 2)
            # data[:, [0, 2]] = data[:, [2, 0]]
        else:
            print('invalid ordermode of mrc files %d' % ordermode)
            exit()
        return map_data

    # def reset_main_chain_prob(self, chain_prob, threshold):
    #     self.print_info()
    #     self.dens.flags.writeable = True
    #     cnt_act = 0
    #     self.dens[self.dens < 0] = 0
    #     density = np.zeros(self.dens.shape)
    #     for i in range(self.shape[0]):
    #         for j in range(self.shape[1]):
    #             for k in range(self.shape[2]):
    #                 if self.dens[i, j, k] < 0:
    #                     continue
    #                 if chain_prob[i, j, k] >= threshold:
    #                     density[i, j, k] = chain_prob[i, j, k]
    #                     cnt_act += 1
    #     self.dens = density
    #     self.Nact = cnt_act

    #     print("dens shape now")
    #     print(self.shape)
    #     print("x dim now %d,ydim now %d, zdim now %d" %
    #           (self.xdim, self.ydim, self.zdim))
    #     print("mrc file mode %d" % self.ordermode)
    #     total = self.shape[0] * self.shape[1] * self.shape[2]
    #     print("in total useful percentage %.6f" % (self.Nact / total))
    #     if self.ordermode == 1:
    #         self.dens = self.dens.swapaxes(0, 2)

    #     elif self.ordermode == 2:
    #         self.dens = self.dens.swapaxes(0, 1)
    #         self.dens = self.dens.swapaxes(0, 2)

    #     elif self.ordermode == 3:
    #         self.dens = self.dens.swapaxes(0, 1)
    #         self.dens = self.dens.swapaxes(1, 2)
    #     elif self.ordermode == 4:

    #         self.dens = self.dens.swapaxes(0, 1)
    #     elif self.ordermode == 5:
    #         self.dens = self.dens.swapaxes(1, 2)
    #     elif self.ordermode == 6:
    #         print('order mode 0 no operation')
    #     else:
    #         print('invalid ordermode of mrc files %d' % self.ordermode)
    #         exit()
    #     print("dens shape now")
    #     print(self.dens.shape)
    #     self.shape = self.dens.shape
    #     print("x dim now %d" % self.xdim)
    #     print("after normalizing dens min %.4f max %.4f" %
    #           (np.min(self.dens), np.max(self.dens)))
    #     return True

    # def upsampling_chain_prob(self, chain_prob, threshold=0.01):

    #     main_chain_prob = chain_prob[1]
    #     main_chain_prob[main_chain_prob <=
    #                     threshold] = 0  #only keep our main chain prediction
    #     main_chain_prob[self.dens <= 0] = 0
    #     main_chain_prob[np.isnan(main_chain_prob)] = 0
    #     self.chain_dens = main_chain_prob
    #     self.chain_Nact = len(np.argwhere(main_chain_prob != 0))
    #     total = self.shape[0] * self.shape[1] * self.shape[2]
    #     print("in total chain useful percentage %.6f" %
    #           (self.chain_Nact / total))
    #     print("dens shape now")
    #     print(self.dens.shape)
    #     self.shape = self.dens.shape
    #     print("after normalizing chain dens min %.4f max %.4f" %
    #           (np.min(self.chain_dens), np.max(self.chain_dens)))
    #     return True

    # def upsampling_sugar_prob(self,
    #                           main_chain_prob,
    #                           threshold=0.01,
    #                           filter_array=None):

    #     #main_chain_prob = nuc_prob[1]
    #     main_chain_prob[main_chain_prob <=
    #                     threshold] = 0  #only keep our main chain prediction
    #     main_chain_prob[self.dens <= 0] = 0
    #     main_chain_prob[np.isnan(main_chain_prob)] = 0
    #     if filter_array is not None:
    #         main_chain_prob[filter_array <= 0] = 0
    #     self.sugar_dens = main_chain_prob
    #     self.sugar_Nact = len(np.argwhere(main_chain_prob != 0))
    #     total = self.shape[0] * self.shape[1] * self.shape[2]
    #     print("useful points: ", self.sugar_Nact)
    #     print("in total chain useful percentage %.6f" %
    #           (self.sugar_Nact / total))
    #     print("dens shape now")
    #     print(self.dens.shape)
    #     self.shape = self.dens.shape
    #     print("after normalizing sugar dens min %.4f max %.4f" %
    #           (np.min(self.sugar_dens), np.max(self.sugar_dens)))
    #     return True

    # def upsampling_pho_prob(self,
    #                         main_chain_prob,
    #                         threshold=0.01,
    #                         filter_array=None):

    #     #main_chain_prob = nuc_prob[2]
    #     main_chain_prob[main_chain_prob <=
    #                     threshold] = 0  #only keep our main chain prediction
    #     main_chain_prob[self.dens <= 0] = 0
    #     main_chain_prob[np.isnan(main_chain_prob)] = 0
    #     if filter_array is not None:
    #         main_chain_prob[filter_array <= 0] = 0
    #     self.pho_dens = main_chain_prob
    #     self.pho_Nact = len(np.argwhere(main_chain_prob != 0))
    #     total = self.shape[0] * self.shape[1] * self.shape[2]
    #     print("useful points: ", self.pho_Nact)
    #     print("in total chain useful percentage %.6f" %
    #           (self.pho_Nact / total))
    #     print("after normalizing pho dens min %.4f max %.4f" %
    #           (np.min(self.pho_dens), np.max(self.pho_dens)))
    #     return True

    # def upsampling_specify_prob(self,
    #                             specify_name,
    #                             main_chain_prob,
    #                             threshold=0.01,
    #                             filter_array=None):

    #     #main_chain_prob = nuc_prob[2]
    #     main_chain_prob[main_chain_prob <=
    #                     threshold] = 0  #only keep our main chain prediction
    #     main_chain_prob[self.dens <= 0] = 0
    #     main_chain_prob[np.isnan(main_chain_prob)] = 0
    #     if filter_array is not None:
    #         main_chain_prob[filter_array <= 0] = 0
    #     names = self.__dict__
    #     names['%s_dens' % specify_name] = main_chain_prob
    #     names["%s_Nact" % specify_name] = len(
    #         np.argwhere(main_chain_prob != 0))
    #     total = self.shape[0] * self.shape[1] * self.shape[2]
    #     print("useful points: ", names["%s_Nact" % specify_name])
    #     print("in total chain useful percentage %.6f" %
    #           (names["%s_Nact" % specify_name] / total))
    #     print("after normalizing pho dens min %.4f max %.4f" %
    #           (np.min(names['%s_dens' % specify_name]),
    #            np.max(names['%s_dens' % specify_name])))
    #     return True

    # def upsampling_patom_prob(self,
    #                           main_chain_prob,
    #                           threshold=0.01,
    #                           filter_array=None):

    #     main_chain_prob[main_chain_prob <=
    #                     threshold] = 0  #only keep our main chain prediction
    #     main_chain_prob[self.dens <= 0] = 0
    #     if filter_array is not None:
    #         main_chain_prob[filter_array <= 0] = 0
    #     self.patom_dens = main_chain_prob
    #     self.patom_Nact = len(np.argwhere(main_chain_prob != 0))
    #     total = self.shape[0] * self.shape[1] * self.shape[2]
    #     print("useful points: ", self.patom_Nact)
    #     print("in total chain useful percentage %.6f" %
    #           (self.patom_Nact / total))
    #     print("after normalizing pho dens min %.4f max %.4f" %
    #           (np.min(self.patom_dens), np.max(self.patom_dens)))
    #     return True

    # def upsampling_based_prob(self, prob_dict, threshold):
    #     Name_list = ["atom", "nuc", "chain", 'base']
    #     self.dens.flags.writeable = True
    #     cnt_act = 0
    #     self.dens[self.dens < 0] = 0
    #     #then normalize the original density
    #     norm_density = self.dens / np.max(self.dens)

    #     density = np.zeros(self.dens.shape)
    #     chain_prob = prob_dict['chain']
    #     atom_prob = prob_dict['atom']
    #     nuc_prob = prob_dict['nuc']
    #     base_prob = prob_dict['base']
    #     for i in range(self.shape[0]):
    #         for j in range(self.shape[1]):
    #             for k in range(self.shape[2]):
    #                 if self.dens[i, j, k] < 0:
    #                     continue
    #                 #must ignore the side chain predictions
    #                 if chain_prob[0, i, j, k] >= threshold:
    #                     #density[i, j, k] = chain_prob[0,i,j,k]
    #                     density[i, j, k] = chain_prob[
    #                         0, i, j,
    #                         k]  #np.sum(nuc_prob[:4,i,j,k]) #only keep the prob of bases
    #                     #norm_density[i,j,k]+np.sum(chain_prob[:2,i,j,k])\
    #                     #+np.sum(atom_prob[:4,i,j,k])+np.sum(nuc_prob[:6,i,j,k])
    #                     cnt_act += 1
    #     # density[chain_prob[0]>=threshold] = norm_density + chain_prob[0]+chain_prob[1]+\
    #     #                                     atom_prob[0]+atom_prob[1]+atom_prob[2] +atom_prob[3]+\
    #     #                                     nuc_prob[0]+nuc_prob[1]+nuc_prob[2]+nuc_prob[3]+nuc_prob[4]+nuc_prob[5]
    #     self.dens = density
    #     self.Nact = cnt_act

    #     print("dens shape now")
    #     print(self.shape)
    #     print("x dim now %d,ydim now %d, zdim now %d" %
    #           (self.xdim, self.ydim, self.zdim))
    #     print("mrc file mode %d" % self.ordermode)
    #     total = self.shape[0] * self.shape[1] * self.shape[2]
    #     print("in total useful percentage %.6f" % (self.Nact / total))
    #     if self.ordermode == 1:
    #         self.dens = self.dens.swapaxes(0, 2)

    #     elif self.ordermode == 2:
    #         self.dens = self.dens.swapaxes(0, 1)
    #         self.dens = self.dens.swapaxes(0, 2)

    #     elif self.ordermode == 3:
    #         self.dens = self.dens.swapaxes(0, 1)
    #         self.dens = self.dens.swapaxes(1, 2)
    #     elif self.ordermode == 4:

    #         self.dens = self.dens.swapaxes(0, 1)
    #     elif self.ordermode == 5:
    #         self.dens = self.dens.swapaxes(1, 2)
    #     elif self.ordermode == 6:
    #         print('order mode 0 no operation')
    #     else:
    #         print('invalid ordermode of mrc files %d' % self.ordermode)
    #         exit()
    #     print("dens shape now")
    #     print(self.dens.shape)
    #     self.shape = self.dens.shape
    #     print("x dim now %d" % self.xdim)
    #     print("after normalizing dens min %.4f max %.4f" %
    #           (np.min(self.dens), np.max(self.dens)))
    #     return True

    # def upsampling(self, map_t):
    #     """
    #     removing points that prob<map_t
    #     :param map_t:
    #     :return:
    #     """
    #     self.print_info()
    #     self.dens.flags.writeable = True
    #     cnt_act = 0
    #     for i in range(self.shape[0]):
    #         for j in range(self.shape[1]):
    #             for k in range(self.shape[2]):
    #                 if self.dens[i, j, k] < map_t:
    #                     self.dens[i, j, k] = 0
    #                 else:
    #                     cnt_act += 1
    #     self.Nact = cnt_act

    #     print("dens shape now")
    #     print(self.shape)
    #     print("x dim now %d,ydim now %d, zdim now %d" %
    #           (self.xdim, self.ydim, self.zdim))
    #     print("mrc file mode %d" % self.ordermode)
    #     total = self.shape[0] * self.shape[1] * self.shape[2]
    #     print("in total useful percentage %.6f" % (self.Nact / total))
    #     if self.ordermode == 1:
    #         self.dens = self.dens.swapaxes(0, 2)

    #     elif self.ordermode == 2:
    #         self.dens = self.dens.swapaxes(0, 1)
    #         self.dens = self.dens.swapaxes(0, 2)

    #     elif self.ordermode == 3:
    #         self.dens = self.dens.swapaxes(0, 1)
    #         self.dens = self.dens.swapaxes(1, 2)
    #     elif self.ordermode == 4:

    #         self.dens = self.dens.swapaxes(0, 1)
    #     elif self.ordermode == 5:
    #         self.dens = self.dens.swapaxes(1, 2)
    #     elif self.ordermode == 6:
    #         print('order mode 0 no operation')
    #     else:
    #         print('invalid ordermode of mrc files %d' % self.ordermode)
    #         exit()
    #     print("dens shape now")
    #     print(self.dens.shape)
    #     self.shape = self.dens.shape
    #     print("x dim now %d" % self.xdim)
    #     print("after normalizing dens min %.4f max %.4f" %
    #           (np.min(self.dens), np.max(self.dens)))
    #     return True

    # def general_mean_shift(self,
    #                        density,
    #                        point,
    #                        mean_shift_path,
    #                        constriant=False):
    #     print('carry on mean shifting jobs')
    #     cnt = 0
    #     for i in range(self.shape[0]):
    #         for j in range(self.shape[1]):
    #             for k in range(self.shape[2]):
    #                 if density[i, j, k] == 0.00:
    #                     continue
    #                 point.cd[cnt][0] = float(i)
    #                 point.cd[cnt][1] = float(j)
    #                 point.cd[cnt][2] = float(k)
    #                 point.origrid[cnt][0] = i
    #                 point.origrid[cnt][1] = j
    #                 point.origrid[cnt][2] = k
    #                 point.ori_dens[cnt] = density[i, j, k]
    #                 cnt += 1
    #     point.Ncd = cnt
    #     point.Nori = cnt
    #     print('useful points %d' % cnt)
    #     print('set up filters')
    #     # Set up filters
    #     bandwidth = self.gaussian_bandwidth  #self.params['g']  # bandwidth of Gaussian distribution
    #     gstep = self.widthx
    #     fs = (bandwidth / gstep) * 0.5
    #     fs = fs * fs
    #     fsiv = 1 / (float(fs))
    #     fmaxd = (bandwidth / gstep) * 2.0
    #     print('fmaxd=%f' % fmaxd)
    #     # Meanshifting
    #     tmp_xdim = (float)(density.shape[0])
    #     tmp_ydim = (float)(density.shape[1])
    #     tmp_zdim = float(density.shape[2])
    #     tmp_dens = np.array(density)
    #     #point.cd: [id]:[x,y,z] in grid space
    #     if not constriant:
    #         point.cd, point.dens = carry_shift(point.cd, cnt, fmaxd, fsiv,
    #                                            tmp_xdim, tmp_ydim, tmp_zdim,
    #                                            tmp_dens)
    #         #point.cd: [id]:[x,y,z] coordinates after shift
    #         cd_path = mean_shift_path + '_cd.txt'
    #         dense_path = mean_shift_path + '_dens.txt'
    #         np.savetxt(cd_path, point.cd)
    #         np.savetxt(dense_path, point.dens)
    #     else:
    #         point.cd, point.dens = carry_shift_limit(point.cd,
    #                                                  cnt,
    #                                                  fmaxd,
    #                                                  fsiv,
    #                                                  tmp_xdim,
    #                                                  tmp_ydim,
    #                                                  tmp_zdim,
    #                                                  tmp_dens,
    #                                                  move_limit=3)
    #         cd_path = mean_shift_path + '_cd_relax.txt'
    #         dense_path = mean_shift_path + '_dens_relax.txt'
    #         np.savetxt(cd_path, point.cd)
    #         np.savetxt(dense_path, point.dens)
    #     print('finishing meanshifting with %d points' % point.Ncd)

    # def mean_shift(self, point, mean_shift_path):
    #     try:
    #         self.dens.flags.writeable = True
    #     except:
    #         print("no need to set write flag for density")
    #     print('carry on mean shifting jobs')
    #     cnt = 0
    #     for i in range(self.shape[0]):
    #         for j in range(self.shape[1]):
    #             for k in range(self.shape[2]):
    #                 if self.dens[i, j, k] == 0.00:
    #                     continue
    #                 point.cd[cnt][0] = float(i)
    #                 point.cd[cnt][1] = float(j)
    #                 point.cd[cnt][2] = float(k)
    #                 point.origrid[cnt][0] = i
    #                 point.origrid[cnt][1] = j
    #                 point.origrid[cnt][2] = k
    #                 point.ori_dens[cnt] = self.dens[i, j, k]
    #                 cnt += 1
    #     point.Ncd = cnt
    #     point.Nori = cnt
    #     print('useful points %d' % cnt)
    #     print('set up filters')
    #     # Set up filters
    #     bandwidth = self.gaussian_bandwidth  #self.params['g']  # bandwidth of Gaussian distribution
    #     gstep = self.widthx
    #     fs = (bandwidth / gstep) * 0.5
    #     fs = fs * fs
    #     fsiv = 1 / (float(fs))
    #     fmaxd = (bandwidth / gstep) * 2.0
    #     print('fmaxd=%f' % fmaxd)
    #     # Meanshifting
    #     tmp_xdim = (float)(self.dens.shape[0])
    #     tmp_ydim = (float)(self.dens.shape[1])
    #     tmp_zdim = float(self.dens.shape[2])
    #     tmp_dens = np.array(self.dens)
    #     #point.cd: [id]:[x,y,z] in grid space
    #     point.cd, point.dens = carry_shift(point.cd, cnt, fmaxd, fsiv,
    #                                        tmp_xdim, tmp_ydim, tmp_zdim,
    #                                        tmp_dens)
    #     #point.cd: [id]:[x,y,z] coordinates after shift
    #     cd_path = mean_shift_path + '_cd.txt'
    #     dense_path = mean_shift_path + '_dens.txt'
    #     np.savetxt(cd_path, point.cd)
    #     np.savetxt(dense_path, point.dens)
    #     print('finishing meanshifting with %d points' % point.Ncd)

    # def load_mean_shift(self, point, mean_shift_path, constraint=False):
    #     print('Load mean shifting results')
    #     cnt = 0
    #     xydim = self.xdim * self.ydim
    #     for i in range(self.shape[0]):
    #         for j in range(self.shape[1]):
    #             for k in range(self.shape[2]):
    #                 if self.dens[i, j, k] == 0.00:
    #                     continue
    #                 point.cd[cnt][0] = float(i)
    #                 point.cd[cnt][1] = float(j)
    #                 point.cd[cnt][2] = float(k)
    #                 point.origrid[cnt][0] = i
    #                 point.origrid[cnt][1] = j
    #                 point.origrid[cnt][2] = k
    #                 point.ori_dens[cnt] = self.dens[i, j, k]
    #                 cnt += 1
    #     point.Ncd = cnt
    #     point.Nori = cnt
    #     if constraint:
    #         cd_path = mean_shift_path + '_cd_relax.txt'
    #         dense_path = mean_shift_path + '_dens_relax.txt'

    #     else:
    #         cd_path = mean_shift_path + '_cd.txt'
    #         dense_path = mean_shift_path + '_dens.txt'
    #     point.cd = np.loadtxt(cd_path)
    #     point.dens = np.loadtxt(dense_path)
    #     print('finishing meanshifting with %d points' % point.Ncd)

    # def load_general_mean_shift(self, density, point, mean_shift_path):
    #     print('Load mean shifting results')
    #     cnt = 0
    #     xydim = self.xdim * self.ydim
    #     for i in range(self.shape[0]):
    #         for j in range(self.shape[1]):
    #             for k in range(self.shape[2]):
    #                 if density[i, j, k] == 0.00:
    #                     continue
    #                 point.cd[cnt][0] = float(i)
    #                 point.cd[cnt][1] = float(j)
    #                 point.cd[cnt][2] = float(k)
    #                 point.origrid[cnt][0] = i
    #                 point.origrid[cnt][1] = j
    #                 point.origrid[cnt][2] = k
    #                 point.ori_dens[cnt] = density[i, j, k]
    #                 cnt += 1
    #     point.Ncd = cnt
    #     point.Nori = cnt

    #     cd_path = mean_shift_path + '_cd.txt'
    #     dense_path = mean_shift_path + '_dens.txt'
    #     point.cd = np.loadtxt(cd_path)
    #     point.dens = np.loadtxt(dense_path)
    #     print('finishing meanshifting with %d points' % point.Ncd)
