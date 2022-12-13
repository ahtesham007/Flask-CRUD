# Flask-CRUD
This Flask-CRUD is starter project.
<p align="center">
  <img width="340" height="160" src="https://miro.medium.com/max/1266/1*vB-cUmm1_dBBt-4JtL0u5g.jpeg">
</p>

--- 

## 🛠️ Installation Steps

Star and Fork the Repo 🌟 and this will keep us motivated.

1. Clone the repository

```bash
git clone https://github.com/ahtesham007/Flask-CRUD.git
```

2. Change the working directory

```bash
cd Flask-CRUD
```

3. Setup Virtual Environment

```bash
python -m venv flask_crud_env
flask_crud_env\Scripts\activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run the app

```bash
python app.py
```

Endpoint      Methods                 Rule
------------  ----------------------  -----------------------
health_check  GET                     /api/v1/
static        GET                     /static/<path:filename>
users_api     DELETE, GET, POST, PUT  /api/v1/users/
