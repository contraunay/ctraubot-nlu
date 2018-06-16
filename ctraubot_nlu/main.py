def train_nlu():
	from rasa_nlu.training_data import load_data
	from rasa_nlu.config import RasaNLUModelConfig
	from rasa_nlu.model import Trainer
	from rasa_nlu import config
	from pathlib import Path

	training_data = load_data('training_data/general-chat.md')
	trainer = Trainer(config.load("training_data/config_spacy_sklearn.yaml"))
	trainer.train(training_data)
	model_directory = trainer.persist(Path('.').parent/"models",
                            project_name='ctraubot',
                            fixed_model_name='nlu') 

if __name__ == '__main__':
	train_nlu()