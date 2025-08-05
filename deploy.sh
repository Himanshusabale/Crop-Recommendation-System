#!/bin/bash

# Crop Recommendation System Deployment Script
echo "🚀 Deploying Crop Recommendation System..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit"
fi

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI not found. Please install it first:"
    echo "   https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

# Check if user is logged into Heroku
if ! heroku auth:whoami &> /dev/null; then
    echo "🔐 Please login to Heroku first:"
    heroku login
fi

# Create Heroku app if it doesn't exist
if [ -z "$HEROKU_APP_NAME" ]; then
    echo "🏗️  Creating Heroku app..."
    heroku create
    export HEROKU_APP_NAME=$(heroku apps:info --json | grep -o '"name":"[^"]*"' | cut -d'"' -f4)
else
    echo "🔗 Using existing Heroku app: $HEROKU_APP_NAME"
    heroku git:remote -a $HEROKU_APP_NAME
fi

# Deploy to Heroku
echo "📤 Deploying to Heroku..."
git add .
git commit -m "Deploy crop recommendation system"
git push heroku main

# Open the app
echo "🌐 Opening the deployed app..."
heroku open

echo "✅ Deployment complete!"
echo "🔗 Your app is now live at: https://$HEROKU_APP_NAME.herokuapp.com"
echo ""
echo "📊 To view logs: heroku logs --tail"
echo "🔧 To restart: heroku restart"
echo "🗑️  To destroy: heroku apps:destroy --app $HEROKU_APP_NAME" 