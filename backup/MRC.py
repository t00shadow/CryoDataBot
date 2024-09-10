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
