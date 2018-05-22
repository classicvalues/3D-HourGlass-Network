import torch
import torch.nn as nn

lossfunc = nn.MSELoss().cuda()

#@torch.set_default_tensor_type('torch.cuda.FloatTensor')

def Joints2DHeatMapsSquaredError(input, target):
	global lossfunc
	"""
	Takes input as (N,C,D,H,W) and similar target (Here C is number of channels equivalent to number of joints
	and H,W are equal to the input image dimensions (i.e. 256 each))
	"""
	assert input.shape == target.shape
	assert len(input.shape) == 5
	assert (input[:,:,0,:,:] == input[:,:,1,:,:]).all()
	input = input.cuda()
	return lossfunc(input, target)

def Joints2DArgMaxSquaredError(input, target):
	global lossfunc
	"""
	Takes input as (N,C,D,2) and similar target (Here C is number of channels equivalent to number of joints)
	"""
	assert input.shape == target.shape
	assert len(input.shape) == 4
	input = input.cuda()
	return lossfunc(input, target)

def JointsDepthSquaredError(input, target):
	global lossfunc
	"""
	Takes input as (N,C,D,1) and similar target (Here C is number of channels equivalent to number of joints)
	"""
	assert input.shape == target.shape
	assert len(input.shape) == 4
	input = input.cuda()
	print(input[0,:,:3,0])
	print(target[0,:,:3,0])
	return lossfunc(input, target)
