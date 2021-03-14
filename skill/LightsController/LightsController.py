from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class LightsController(AliceSkill):
	"""
	Author: Team5
	Description: A skill to control your zigbee lights
	"""

	
	@IntentHandler('toggleLightOn')
	def toggleOnIntent(self, session: DialogSession, **_kwargs):
		self.endDialog(session.sessionId, self.randomTalk(text='toggleOn'))


	@IntentHandler('toggleLightOff')
	def toggleOffIntent(self, session: DialogSession, **_kwargs):
		self.endDialog(session.sessionId, self.randomTalk(text='toggleOff'))

	@IntentHandler('changeColor')
	def changeColorIntent(self, session: DialogSession, **_kwargs):
		self.endDialog(session.sessionId, self.randomTalk(text='changeColor'))
