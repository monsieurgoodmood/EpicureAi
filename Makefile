reinstall_package:
	@pip install -e .

run_train:
	python -c 'from ml_logic/train import train_model; train()'
