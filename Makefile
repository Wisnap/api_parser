init:
	pip install -U -r requirements.txt

report:
	mkdir -p "reports"
	python -c "from app.ozon_analytics_data import main; main()"