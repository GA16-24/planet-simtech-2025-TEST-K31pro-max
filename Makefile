.PHONY: model test report presentation verify clean-tmp

model:
	.venv/bin/python model/run_all.py

test:
	.venv/bin/python -m unittest discover -s model -p 'test_*.py' -v

report:
	bash scripts/build_report.sh

presentation:
	bash scripts/build_presentation.sh

verify: test
	.venv/bin/python scripts/verify_report.py
	.venv/bin/python scripts/verify_presentation.py
	.venv/bin/python scripts/verify_repository.py

review-package:
	.venv/bin/python scripts/package_review.py

clean-tmp:
	rm -rf tmp/report_pages tmp/presentation_pages tmp/video_build
