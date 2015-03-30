"""
The AbstractSceneAtmospheric class provides an interface to editing
atmosperhics in a Scene environment for any DCC application

"""


from blur3d	import abstractmethod
from blur3d.api import SceneWrapper
from blur3d import api
from blur3d.constants import EnvironmentTypes


class AbstractSceneAtmospheric(SceneWrapper):
	#------------------------------------------------------------------------------------------------------------------------
	# 												protected methods
	#------------------------------------------------------------------------------------------------------------------------
	@abstractmethod
	def _nativeLayer(self):
		"""
			\remarks	return the layer that this atmospheric is a part of
			\sa			layer
			\return		<variant> nativeLayer || None
		"""
		return None

	#------------------------------------------------------------------------------------------------------------------------
	# 												public methods
	#------------------------------------------------------------------------------------------------------------------------
	def disable(self):
		"""Disables this atmospheric in the scene
		
		:return: True if successful
		
		.. seealso:: :meth:`enable`, :meth:`isEnabled`, :meth:`setEnabled`

		"""
		return self.setEnabled(False)

	def enable(self):
		"""Enables this atmospheric in the scene
		
		:return: True if successful
		
		.. seealso:: :meth:`disable`, :meth:`isEnabled`, :meth:`setEnabled`
				

		"""
		return self.setEnabled(True)

	def environmentType(self):
		return EnvironmentTypes.Unknown

	def index(self):
		""" Returns the index of the atmosperhic
		
		Returns:
			int: Returns -1 if invalid
		"""
		return -1

	@abstractmethod
	def isEnabled(self):
		"""Return whether or not this atmospheric is currently 
		enabled in the scene
		
		:return: True if enabled
		
		.. seealso:: :meth:`disable`, :meth:`enable`, :meth:`setEnabled`

		"""
		return False

	def layer(self):
		"""Return the layer that this atmospheric is a part of
		
		:return: :class:`blur3d.api.SceneLayer` or None
			
		"""
		nativeLayer = self._nativeLayer()
		if (nativeLayer):
			from blur3d.api import SceneLayer
			return SceneLayer(self._scene, nativeLayer)
		return None

	def remove(self):
		""" Removes this atmosperhic from the scene
		
		Returns:
			bool: Was the object removed
		"""
		return False

	def scene(self):
		"""Return the scene instance that this atmospheric is linked to
		
		:return: :class:`blur3d.api.Scene` or None
		
		"""
		return self._scene

	@abstractmethod
	def setEnabled(self, state):
		"""Set whether or not this atmospheric is currently enabled 
		in the scene
		
		:return: True if successful
		
		"""
		return False

	@classmethod
	def fromXml(cls, scene, xml):
		"""Restore the atmospheric from the inputed xml node
		
		:param scene: :class:`blur3d.api.Scene`
		:param xml: :class:`blurdev.XML.XMLElement`
		:return: :class:`blurdev.api.SceneAtmospheric` or None
		
		"""
		return scene.findAtmospheric(name=xml.attribute('name'), uniqueId=int(xml.attribute('id', 0)))


# register the symbol
api.registerSymbol('SceneAtmospheric', AbstractSceneAtmospheric, ifNotFound=True)
