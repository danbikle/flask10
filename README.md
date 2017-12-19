# README.md

How to deploy this site to Heroku.com and Ubuntu

I created an account on the heroku.com website and memorized my password there.

Then from a terminal, not emacs-shell, I ran some shell commands:

```bash
cd ~
rm -f Anaconda*sh
rm -rf anaconda3
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
bash Anaconda3-5.0.1-Linux-x86_64.sh
mv anaconda3/bin/curl anaconda3/bin/curl_ana
echo 'export PATH=${HOME}/anaconda3/bin:$PATH' >> ~/.bashrc
bash
conda install gunicorn
```

```bash
cd ~
rm -rf heroku.tar.gz heroku heroku-client.tgz heroku-client heroku-linux-amd64.tar.gz
wget https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli-linux-x64.tar.gz -O heroku.tar.gz
tar xf heroku.tar.gz
mv heroku*linux-x64 heroku
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
