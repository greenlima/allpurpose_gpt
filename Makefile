#################### PACKAGE ACTIONS ###################

reinstall_package:
	@pip uninstall -y allpurpose_gpt || :
	@pip install -e .

run_gpt:
	chainlit run interface/main.py
