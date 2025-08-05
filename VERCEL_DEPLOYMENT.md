# Vercel Deployment Guide

This guide will help you deploy your Crop Recommendation System to Vercel without installation errors.

## 🚀 **Quick Deploy to Vercel**

### **Step 1: Prepare Your Repository**

1. **Ensure you have the correct files:**
   - `vercel.json` - Vercel configuration
   - `requirements.txt` - Python dependencies (optimized for Vercel)
   - `app.py` - Flask application
   - `templates/index.html` - Web interface

2. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Optimize for Vercel deployment"
   git push origin main
   ```

### **Step 2: Deploy to Vercel**

1. **Go to [vercel.com](https://vercel.com)**
2. **Sign up/Login with GitHub**
3. **Click "New Project"**
4. **Import your GitHub repository**
5. **Configure the project:**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave empty)
   - **Build Command**: Leave empty
   - **Output Directory**: Leave empty
   - **Install Command**: `pip install -r requirements.txt`

6. **Click "Deploy"**

## 🔧 **Troubleshooting**

### **If you get pip installation errors:**

1. **Check your requirements.txt** - Make sure it only contains:
   ```
   Flask==2.3.3
   pandas==1.5.3
   numpy==1.24.3
   scikit-learn==1.3.0
   ```

2. **The app now uses RandomForest instead of LightGBM** for better Vercel compatibility

3. **Use the vercel.json configuration** provided in this repository

### **If the app doesn't load:**

1. **Check the Vercel logs** in your dashboard
2. **Ensure app.py is in the root directory**
3. **Verify the vercel.json configuration**

## 📁 **File Structure for Vercel**

```
your-repo/
├── app.py                 # Main Flask app
├── vercel.json           # Vercel configuration
├── requirements.txt      # Python dependencies (optimized)
├── templates/
│   └── index.html       # Web interface
├── crop_model.pkl       # ML model (optional)
└── README.md
```

## ⚙️ **Vercel Configuration (vercel.json)**

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "FLASK_ENV": "production",
    "FLASK_DEBUG": "0"
  }
}
```

## 🎯 **Alternative: Railway Deployment**

If Vercel continues to have issues, try **Railway** instead:

1. **Go to [railway.app](https://railway.app)**
2. **Connect your GitHub repository**
3. **Railway will automatically detect it's a Python app**
4. **Deploy with one click**

Railway is often more reliable for Flask applications and doesn't have the dependency issues.

## 🔍 **Common Issues & Solutions**

### **Issue: "pip installation failed"**
**Solution**: Use the optimized requirements.txt with lighter dependencies

### **Issue: "Module not found"**
**Solution**: Ensure all dependencies are in requirements.txt

### **Issue: "Build failed"**
**Solution**: Check Vercel logs and ensure app.py is in the root directory

### **Issue: "Function timeout"**
**Solution**: The model training might take too long. Consider pre-training the model.

## 📊 **Monitoring Your Deployment**

1. **Vercel Dashboard**: Monitor deployments and logs
2. **Function Logs**: Check for any runtime errors
3. **Performance**: Monitor response times

## 🚀 **Quick Commands**

```bash
# Install Vercel CLI (optional)
npm i -g vercel

# Deploy from command line
vercel

# Deploy to production
vercel --prod
```

## ✅ **Success Indicators**

- ✅ Build completes without errors
- ✅ App loads at your Vercel URL
- ✅ Predictions work correctly
- ✅ No pip installation errors

Your app should be live at: `https://your-app-name.vercel.app`

## 🔄 **Changes Made for Vercel Compatibility**

1. **Replaced LightGBM with RandomForest** - Lighter, more compatible
2. **Optimized dependencies** - Removed heavy packages
3. **Updated model training** - Uses scikit-learn instead of LightGBM
4. **Maintained functionality** - Same features, better compatibility 