from nibabel import nb

	nb.load("mni_template.nii.gz")
	
	print(nii.header)