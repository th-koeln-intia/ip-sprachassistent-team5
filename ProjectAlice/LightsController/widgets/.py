import sqlite3
from core.base.model.Widget import Widget
from core.base.model.Widget import WidgetSizes


class (Widget):

	SIZE = WidgetSizes.w_small
	OPTIONS = dict()

	def __init__(self, data: sqlite3.Row):
		super().__init__(data)