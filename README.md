Vigneshwaran S - Personal Portfolio Website

A high-impact, recruiter-optimized portfolio website built with React, Tailwind CSS, and Vite. This project features a modern design, dark mode, and a unique AI Recruiter Assistant powered by Google's Gemini API to interact with visitors.

🚀 Features

Recruiter-Optimized UI: Sticky navigation, clear CTAs, and a clean "Above the Fold" introduction.

AI Assistant Integration: A built-in chatbot (powered by Gemini) that answers questions about your skills and analyzes Job Descriptions to find a match.

Dark/Light Mode: Fully supported with a toggle switch.

Responsive Design: Mobile-first approach ensuring it looks great on all devices.

Project Showcase: structured to highlight the Problem, Solution, and Impact of your work.

Smooth Animations: Professional scroll-reveal and interaction animations.

🛠️ Tech Stack

Frontend: React.js (Vite)

Styling: Tailwind CSS

Icons: Lucide React

AI Integration: Google Gemini API (gemini-2.5-flash-preview)

🏁 Getting Started

Follow these steps to get a local copy up and running.

Prerequisites

Node.js (v18 or higher recommended)

npm (comes with Node.js)

Installation

Clone the repository (or unzip the project folder):

git clone [https://github.com/yourusername/portfolio-website.git](https://github.com/yourusername/portfolio-website.git)
cd portfolio-website


Install dependencies:

npm install


Start the development server:

npm run dev


Open your browser:
Navigate to http://localhost:5173 (or the port shown in your terminal).

🔑 Setting up the AI Feature (Gemini API)

To make the "Recruiter Assistant" chat feature work, you need a Google Gemini API key.

Get a free API key from Google AI Studio.

Open src/App.jsx.

Locate the RecruiterAI component (around line 170).

Find the apiKey variable and paste your key:

// Inside callGemini function
const apiKey = "YOUR_PASTED_API_KEY_HERE"; 


(Note: For a public GitHub repository, it is recommended to use Environment Variables (.env) instead of hardcoding the key).

🎨 Customization

All personal data is stored in clear JavaScript objects at the top of src/App.jsx. You can easily update:

personalInfo: Name, tagline, contact links.

skills: Your technical stack and proficiency levels.

projects: Add new projects following the { title, problem, solution... } structure.

experiences: Update your internship or work history.

📦 Deployment

This project is optimized for deployment on Netlify, Vercel, or GitHub Pages.

To build for production:

npm run build


This will create a dist folder containing the static files ready for upload.

📄 License

This project is open source and available under the MIT License.