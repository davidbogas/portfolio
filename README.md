# Developer portfolio

<h2>Project description</h2>

<p>
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=FFFFFF" alt="Django" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD343" alt="Python" />
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" />
    <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="Javascript" />
</p>

<p>
Portfolio webpage made using Django 5.1.1 and Python 3.10.4.
</p>

<p>
Some of the functionalities implemented:
</p>

<ul>
    <li>Models for projects developed, skills, experience and education</li>
    <li>Models for contact info</li>
    <li>Color customization</li>
    <li>Responsive design</li>
    <li>Support for english and spanish languages</li>
</ul>

## How to install

<p>
This project uses <strong>MySQL</strong> as database. Make sure to install MySQL, create a new database and grant privileges to the user you want to use.
</p>

<p>
The project uses dotenv for environment variables. You will need to create a <strong>.env</strong> file next to the <strong>manage.py</strong> file with the following variables:
</p>

```
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=1 (1 for True, 0 for False)
ALLOWED_HOSTS=your.domain.com

DB_NAME=database_name
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=database_host
DB_PORT=database_port
```

<p>
Also, check the paths set in the settings.py file for media and static files. You will need to create the following directories at the root (same level as the project folder):
</p>

```shell
$ mkdir site site/public site/public/media site/public/static
```

<p>
Don't forget to run collectstatic and migrate commands.
</p>

## Show your support

Give it a ⭐️ if you like it.