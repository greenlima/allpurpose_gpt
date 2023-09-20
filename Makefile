#################### PACKAGE ACTIONS ###################

install_allpurpose_gpt:
	@pip uninstall -y allpurpose_gpt || :
	@pip install -e .

run_allpurpose_gpt:
	chainlit run interface/main.py
