import pickle
import src.logger as lg

def save(obj,fname,flag):
	try:
		with open(fname,flag) as f:
			pickle.dump(obj,f)
	except Exception as e:
		lg.log_terminal_only('DSKFY','ERROR',str(e))


def load(fname):
	try:
		with open(fname,'rb') as f:
			return pickle.load(f)
	except Exception as e:
		lg.log_terminal_only('DSKFY','ERROR',str(e))

