##
#	\namespace	blur3d.api.studiomax.studiomaxsceneobject
#
#	\remarks	The StudiomaxSceneModel class provides the implementation of the AbstractSceneModel class as it applies
#				to 3d Studio Max scenes
#	
#	\author		douglas@blur.com
#	\author		Blur Studio
#	\date		06/27/11
#

from blur3d.api.abstract.abstractscenemodel import AbstractSceneModel

#------------------------------------------------------------------------------------------------------------------------

class StudiomaxSceneModel( AbstractSceneModel ):

	def setDisplayName(self, displayName):
		for obj in self.objects():
			nativePointer = obj.nativePointer()
			nativePointer.name = nativePointer.name.replace(self.displayName(), displayName)
		self._nativePointer.name = displayName
		return True

	def objects(self, wildcard='*', type=''):
		objects = self._scene.objects(wildcard='%s.%s' % (self.displayName(), wildcard), type=type)
		return objects

	def setResolution(self, resolution):
		self.userProps()['resolution'] = resolution
		return True

	def resolution(self):
		return self.userProps().get('resolution', '')

# register the symbol
from blur3d import api
api.registerSymbol( 'SceneModel', StudiomaxSceneModel )

