class kbbiRouter(object):
	"""
	A router to control all database operations on models in the
	kbbi application.
	"""
	def db_for_read(self, model, **hints):
		"""
		Attempts to read kbbi models go to kbbi.
		"""
		if model._meta.app_label == 'kbbi':
			return 'kbbi_db'
		return None

	def db_for_write(self, model, **hints):
		"""
		Attempts to write kbbi models go to kbbi.
		"""
		if model._meta.app_label == 'kbbi':
			return 'kbbi_db'
		return None

	def allow_relation(self, obj1, obj2, **hints):
		"""
		Allow relations if a model in the kbbi app is involved.
		"""
		if obj1._meta.app_label == 'kbbi' or obj2._meta.app_label == 'kbbi':
			return True
		return None

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		"""
		Make sure the kbbi app only appears in the 'kbbi'
		database.
		"""
		if app_label == 'kbbi':
			return db == 'kbbi_db'
		return None