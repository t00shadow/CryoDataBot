i manually copied the directory structure of grayson's testing files
DELETE that folder later (in this folder and in my cryodatabot vscode folder) cuz holy shit thats 3 gbs each

also i modified downloading_and_preprocessing.py (test_map.py uses it for normalization if you have normalization toggled on) to allow for it to work even without and nvidia gpu. basically just conditionally uses numpy or cupy and conditionally imports the regular or cupy version of scipy.ndimage binary_dilation and zoom. 

Note i also added a if xp == np: check in the middle of the map_normalizing() function. BUT did not do the same thing for preprocess_one_map() function. may need to do that but seems like this fxn isnt called so ehh. It's only called by preprocess_maps() which is called by downloading_and_preprocessing(). EDIT: i just went ahead and preemptively made the change

might as need to change line 406: protein_tag = xp.asnumpy(binary_dilation(protein_tag, structure=structure).astype(np.int8)) 
to 
if xp == np:
    protein_tag = binary_dilation(protein_tag, structure=structure).astype(np.int8)
else:
    protein_tag = xp.asnumpy(binary_dilation(protein_tag, structure=structure).astype(np.int8))

EDIT: see edit comment above (copied again here). "i just went ahead and preemptively made the change"