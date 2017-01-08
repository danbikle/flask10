# README.md

How to deploy this site to Heroku.com and Ubuntu

I created an account on the heroku.com website and memorized my password there.

Then I ran some shell commands:

```bash
cd ~
rm -f Anaconda3-4.2.0-Linux-x86_64.sh
wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
bash Anaconda3-4.2.0-Linux-x86_64.sh
mv anaconda3/bin/curl anaconda3/bin/curl_ana
echo 'export PATH=${HOME}/anaconda3/bin:$PATH' >> ~/.bashrc
bash
conda install gunicorn
```

```bash
rm -rf heroku heroku-client.tgz heroku-client
wget https://cli-assets.heroku.com/branches/stable/heroku-linux-amd64.tar.gz
tar zxf heroku-linux-amd64.tar.gz
echo 'export PATH=${HOME}/heroku/bin:$PATH' >> ~/.bashrc
bash
heroku auth:login
heroku status
```

I thought of an ORIGINAL name from my new heroku app.

I picked: myflask10

You should pick a different name.

```bash
cd ~
git clone https://github.com/danbikle/flask10 myflask10
cd            myflask10
heroku create myflask10
git push heroku master
heroku ps:scale web=1
```

At that point a gunicorn webserver was running in my heroku deployment.

I saw evidence of this from the shell commands below:

```bash
curl https://myflask10.herokuapp.com/static/home.html
heroku logs
```

To run this app on my laptop, I ran this shell command:

```bash
python flask10.py
```

Which allows me to see the app at the URL listed below:

http://0.0.0.0:5000/static/home.html

Also I can rely on the Gunicorn web server instead of plain Python by using this shell command:

```bash
gunicorn wsgi
```

Which allows me to see the app at the URL listed below:

http://0.0.0.0:8000/static/home.html

On my laptop, if I want to run a server which 'auto-reloads' after each file change, I should start the server with these shell commands:

```bash
cd ~/myflask10
export FLASK_DEBUG=1
export FLASK_APP=flask10.py
flask run
```

If you have questions, e-me: bikle101@gmail.com
