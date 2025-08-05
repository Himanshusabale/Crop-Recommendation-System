# Deployment Guide

This guide covers multiple deployment options for your Crop Recommendation System.

## 🚀 **Option 1: Heroku (Recommended for beginners)**

### Prerequisites
- GitHub account
- Heroku account (free tier available)

### Steps:

1. **Create a GitHub repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/crop-recommendation-system.git
   git push -u origin main
   ```

2. **Deploy to Heroku:**
   ```bash
   # Install Heroku CLI
   # Download from: https://devcenter.heroku.com/articles/heroku-cli
   
   # Login to Heroku
   heroku login
   
   # Create Heroku app
   heroku create your-crop-recommendation-app
   
   # Deploy
   git push heroku main
   
   # Open the app
   heroku open
   ```

3. **Your app will be available at:**
   ```
   https://your-crop-recommendation-app.herokuapp.com
   ```

---

## 🌐 **Option 2: Railway (Alternative to Heroku)**

### Steps:

1. **Go to [Railway.app](https://railway.app)**
2. **Connect your GitHub repository**
3. **Railway will automatically detect it's a Python app**
4. **Deploy with one click**

---

## ☁️ **Option 3: Google Cloud Platform (GCP)**

### Prerequisites
- Google Cloud account
- Google Cloud SDK installed

### Steps:

1. **Create a new project in GCP Console**

2. **Enable App Engine API**

3. **Create app.yaml file:**
   ```yaml
   runtime: python311
   entrypoint: gunicorn -b :$PORT app:app
   
   instance_class: F1
   
   automatic_scaling:
     target_cpu_utilization: 0.65
     min_instances: 1
     max_instances: 10
   ```

4. **Deploy:**
   ```bash
   gcloud app deploy
   ```

---

## 🐳 **Option 4: Docker Deployment**

### Create Dockerfile:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

### Build and run:
```bash
docker build -t crop-recommendation .
docker run -p 5000:5000 crop-recommendation
```

---

## 🖥️ **Option 5: Local Server (VPS)**

### Using Ubuntu/Debian:

1. **Update system:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Python and dependencies:**
   ```bash
   sudo apt install python3 python3-pip python3-venv nginx -y
   ```

3. **Create application directory:**
   ```bash
   mkdir /var/www/crop-recommendation
   cd /var/www/crop-recommendation
   ```

4. **Upload your files and setup:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Create systemd service:**
   ```bash
   sudo nano /etc/systemd/system/crop-recommendation.service
   ```

   Add this content:
   ```ini
   [Unit]
   Description=Crop Recommendation System
   After=network.target

   [Service]
   User=www-data
   WorkingDirectory=/var/www/crop-recommendation
   Environment="PATH=/var/www/crop-recommendation/venv/bin"
   ExecStart=/var/www/crop-recommendation/venv/bin/gunicorn --workers 3 --bind unix:crop-recommendation.sock -m 007 app:app

   [Install]
   WantedBy=multi-user.target
   ```

6. **Start the service:**
   ```bash
   sudo systemctl start crop-recommendation
   sudo systemctl enable crop-recommendation
   ```

7. **Configure Nginx:**
   ```bash
   sudo nano /etc/nginx/sites-available/crop-recommendation
   ```

   Add this content:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           include proxy_params;
           proxy_pass http://unix:/var/www/crop-recommendation/crop-recommendation.sock;
       }
   }
   ```

8. **Enable the site:**
   ```bash
   sudo ln -s /etc/nginx/sites-available/crop-recommendation /etc/nginx/sites-enabled
   sudo nginx -t
   sudo systemctl restart nginx
   ```

---

## 🔧 **Environment Variables**

For production, consider setting these environment variables:

```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
```

---

## 📊 **Monitoring and Logs**

### Heroku:
```bash
heroku logs --tail
```

### Local server:
```bash
sudo journalctl -u crop-recommendation -f
```

---

## 🔒 **Security Considerations**

1. **HTTPS**: Always use HTTPS in production
2. **Environment Variables**: Store sensitive data in environment variables
3. **Rate Limiting**: Consider adding rate limiting for the API
4. **Input Validation**: The current app has basic validation, but consider adding more robust validation

---

## 🚀 **Quick Deploy Commands**

### For Heroku (easiest):
```bash
# 1. Create GitHub repo and push code
git init && git add . && git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/crop-recommendation-system.git
git push -u origin main

# 2. Deploy to Heroku
heroku create your-app-name
git push heroku main
heroku open
```

### For Railway:
1. Go to [railway.app](https://railway.app)
2. Connect GitHub repo
3. Deploy automatically

---

## 📱 **Custom Domain**

After deployment, you can add a custom domain:

### Heroku:
```bash
heroku domains:add yourdomain.com
```

### Update DNS records as instructed by the platform.

---

## 🎯 **Recommended for Beginners**

**Start with Heroku or Railway** - they're the easiest to deploy and maintain. Both offer:
- Free tiers
- Automatic deployments from GitHub
- Built-in SSL certificates
- Easy scaling

Choose the option that best fits your needs and technical expertise! 