import json
import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def load_db():
    with open(os.path.join(DATA_DIR, 'equipment_db.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

def load_routes():
    with open(os.path.join(DATA_DIR, 'routes_db.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    db = load_db()
    return render_template('index.html', categories=db, title='户外装备入门指南')

@app.route('/category/<category_id>')
def category_detail(category_id):
    db = load_db()
    if category_id not in db:
        return '品类不存在', 404
    category = db[category_id]
    cat_name = category.get('name', category_id)
    return render_template('category.html', category=category, category_id=category_id,
                          title=cat_name + ' - 户外装备入门指南')

@app.route('/api/categories')
def api_categories():
    db = load_db()
    return jsonify({'success': True, 'data': db})

@app.route('/api/recommend', methods=['POST'])
def api_recommend():
    db = load_db()
    budget = request.json.get('budget', 5000)
    level = request.json.get('level', '')
    recommendations = {}
    for key, cat in db.items():
        models = []
        for brand in cat.get('brands', []):
            for model in brand.get('recommended_models', []):
                mprice = model.get('price', 0)
                mlevel = model.get('level', '')
                if mprice > budget:
                    continue
                if level and level != 'all' and mlevel != level:
                    continue
                models.append(dict(model, brand=brand['name'], category=cat['name']))
        models.sort(key=lambda x: x.get('price', 0))
        if models:
            recommendations[key] = {'category_name': cat['name'], 'models': models[:5]}
    return jsonify({'success': True, 'data': recommendations, 'budget': budget, 'level': level})

@app.route('/guide')
def guide():
    return render_template('guide.html', title='新手入门指南 - 户外装备入门指南')

@app.route('/compare')
def compare():
    db = load_db()
    return render_template('compare.html', categories=db, title='装备对比 - 户外装备入门指南')

@app.route('/checklist')
def checklist():
    return render_template('checklist.html', title='装备清单生成器 - 户外装备入门指南')

@app.route('/routes')
def routes():
    routes_db = load_routes()
    return render_template('routes.html', routes=routes_db, title='著名徒步路线 - 户外装备入门指南')

@app.route('/route/<route_id>')
def route_detail(route_id):
    routes_db = load_routes()
    if route_id not in routes_db:
        return '路线不存在', 404
    route = routes_db[route_id]
    return render_template('route_detail.html', route=route, route_id=route_id,
                          title=route['name'] + ' - 户外装备入门指南')

@app.route('/api/routes')
def api_routes():
    routes_db = load_routes()
    return jsonify({'success': True, 'data': routes_db})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
