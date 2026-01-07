import os

# Define the project structure and file contents
project_name = "portfolio-website"

files = {
    "package.json": """
{
  "name": "portfolio-website",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "lucide-react": "^0.344.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.64",
    "@types/react-dom": "^18.2.21",
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.18",
    "eslint": "^8.57.0",
    "eslint-plugin-react": "^7.34.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "postcss": "^8.4.35",
    "tailwindcss": "^3.4.1",
    "vite": "^5.1.4"
  }
}
""",
    "vite.config.js": """
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})
""",
    "tailwind.config.js": """
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
}
""",
    "postcss.config.js": """
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
""",
    "index.html": """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vigneshwaran S | Portfolio</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
""",
    "src/index.css": """
@tailwind base;
@tailwind components;
@tailwind utilities;

html {
  scroll-behavior: smooth;
}
""",
    "src/main.jsx": """
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
""",
    "src/App.jsx": """
import React, { useState, useEffect, useRef } from 'react';
import { 
  Github, 
  Linkedin, 
  Mail, 
  FileText, 
  ExternalLink, 
  Code, 
  Server, 
  Shield, 
  Database,
  Terminal,
  Moon,
  Sun,
  Menu,
  X,
  ChevronDown,
  Sparkles,
  MessageSquare,
  Briefcase,
  Send,
  Loader2,
  Bot
} from 'lucide-react';

// --- Data based on User Resume ---

const personalInfo = {
  name: "Vigneshwaran S",
  role: "Fresher Software Developer",
  tagline: "Python | Web Development | Cybersecurity",
  summary: "Motivated Software Developer with hands-on experience in Python and Django-based web development. Skilled in building responsive web applications, debugging backend systems, and creating security tools. Seeking to contribute to scalable software solutions.",
  email: "kssvicky6@gmail.com",
  phone: "+91 6369220562",
  location: "Tamil Nadu, India",
  linkedin: "https://linkedin.com/in/vigneshwarans", 
  github: "https://github.com/vigneshwarans", 
  resumeLink: "/resume.pdf" 
};

const skills = {
  languages: [
    { name: "Python", level: 90 },
    { name: "JavaScript", level: 80 },
    { name: "HTML5/CSS3", level: 95 },
    { name: "SQL", level: 75 }
  ],
  frameworks: [
    { name: "Django", level: 85 },
    { name: "React", level: 70 },
    { name: "Tailwind CSS", level: 90 },
    { name: "Bootstrap", level: 85 }
  ],
  tools: [
    { name: "Git & GitHub", icon: <Code size={16} /> },
    { name: "VS Code", icon: <Code size={16} /> },
    { name: "Linux", icon: <Terminal size={16} /> },
    { name: "Postman", icon: <Server size={16} /> }
  ],
  core: [
    "OOP", "Data Structures", "REST APIs", "Cybersecurity Basics", "SDLC"
  ]
};

const experiences = [
  {
    company: "Mech-tech",
    role: "Full Stack Developer Intern",
    period: "2025",
    description: "Developed and maintained frontend and backend features using Python and Django.",
    achievements: [
      "Debugged backend modules to resolve runtime errors, improving app stability.",
      "Implemented secure forms and database queries.",
      "Collaborated with the team using Git for version control."
    ]
  },
  {
    company: "Hifill Technologies",
    role: "Software Intern",
    period: "May 2025",
    description: "Assisted in frontend and backend development for client-based web applications.",
    achievements: [
      "Identified and fixed UI and backend logic bugs.",
      "Supported feature updates in an Agile environment.",
      "Conducted functionality testing for client deliverables."
    ]
  }
];

const projects = [
  {
    title: "Web App Vulnerability Scanner",
    category: "Cybersecurity / Python",
    problem: "Manual detection of common web vulnerabilities like SQL Injection and XSS is time-consuming and error-prone.",
    solution: "Designed a Python-based automated scanner that analyzes HTTP responses and error patterns to detect security flaws.",
    techStack: ["Python", "Requests Library", "HTTP Protocols"],
    impact: "Strengthened secure coding practices and automated the initial phase of security auditing.",
    links: { github: "#", demo: "#" }
  },
  {
    title: "Penetration Testing Toolkit",
    category: "Network Security",
    problem: "Security professionals need quick access to modular tools for network reconnaissance.",
    solution: "Developed a modular toolkit including a port scanner, directory brute-forcer, and login tester.",
    techStack: ["Python", "Socket Programming", "Automation"],
    impact: "Improved system behavior analysis and reduced time for initial network enumeration.",
    links: { github: "#", demo: "#" }
  },
  {
    title: "Conference Website",
    category: "Frontend Development",
    problem: "Need for a responsive, accessible platform to host event details and schedules.",
    solution: "Built a fully responsive website using modern HTML/CSS and JavaScript for interactivity.",
    techStack: ["HTML5", "CSS3", "JavaScript"],
    impact: "Delivered a clean UI that adapts seamlessly to mobile and desktop devices.",
    links: { github: "#", demo: "#" }
  }
];

const education = [
  {
    degree: "Bachelor of Computer Science",
    institution: "Pursuing",
    year: "2025",
    details: "Focus on Software Engineering and Security."
  },
  {
    degree: "Diploma in Civil Engineering",
    institution: "Completed",
    year: "2020 - 2022",
    details: "Percentage: 95%"
  }
];

const certifications = [
  "Full Stack Development (Django) - Naan Muthalvan",
  "Python Programming - GUVI",
  "Cybersecurity Analyst Job Simulation - Forage",
  "White Hat Hacker & Penetration Testing - Eduonix",
  "SQL Injection Attacks - EC-Council"
];

// --- Gemini API Component ---

const RecruiterAI = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [activeTab, setActiveTab] = useState('chat'); // 'chat' or 'match'
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    { role: 'ai', text: "Hi! I'm Vigneshwaran's AI Assistant. Ask me anything about his skills or experience!" }
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, activeTab]);

  const callGemini = async (prompt, isJobMatch = false) => {
    const apiKey = ""; // Runtime environment provides this
    const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`;

    const contextData = JSON.stringify({
      personalInfo,
      skills,
      experiences,
      projects,
      education,
      certifications
    });

    let systemInstruction = "";
    if (isJobMatch) {
      systemInstruction = `You are an expert technical recruiter assistant for Vigneshwaran S. 
      Analyze the provided Job Description against Vigneshwaran's profile data: ${contextData}.
      Provide a response in this specific format:
      1. **Match Score**: (Estimate 0-100% based on keywords)
      2. **Why he fits**: (3 concise bullet points linking his specific projects/skills to the JD)
      3. **Gap Analysis**: (1 honest but constructive point about what might be missing or transferable)
      Keep the tone professional, encouraging, and honest.`;
    } else {
      systemInstruction = `You are Vigneshwaran S's AI portfolio assistant. 
      You are answering questions from a recruiter or hiring manager.
      Here is Vigneshwaran's full profile data: ${contextData}.
      Rules:
      1. Be professional, confident, and concise (under 3 sentences usually).
      2. Highlight specific projects or internships from the data to prove your points.
      3. If the answer isn't in the data, politely say you don't have that info but suggest contacting him directly via email.
      4. Speak in the first person (as the AI representing him, or "Vigneshwaran has...").`;
    }

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          contents: [{ parts: [{ text: prompt }] }],
          systemInstruction: { parts: [{ text: systemInstruction }] }
        })
      });

      const data = await response.json();
      const text = data.candidates?.[0]?.content?.parts?.[0]?.text || "Sorry, I couldn't process that request right now.";
      return text;
    } catch (error) {
      console.error("Gemini API Error:", error);
      return "I'm having trouble connecting to the server. Please try again later.";
    }
  };

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = input;
    setInput('');
    setIsLoading(true);

    if (activeTab === 'chat') {
      setMessages(prev => [...prev, { role: 'user', text: userMessage }]);
      const response = await callGemini(userMessage, false);
      setMessages(prev => [...prev, { role: 'ai', text: response }]);
    } else {
      // Job Match Logic - treating input as JD
      const response = await callGemini(userMessage, true);
      setMessages([{ role: 'ai', text: response }]); // Clear previous chat for clean result
    }

    setIsLoading(false);
  };

  return (
    <div className="fixed bottom-6 right-6 z-50 flex flex-col items-end pointer-events-none">
      {/* Modal */}
      <div 
        className={`pointer-events-auto bg-white dark:bg-gray-800 rounded-2xl shadow-2xl border border-gray-200 dark:border-gray-700 w-80 sm:w-96 mb-4 transition-all duration-300 origin-bottom-right overflow-hidden ${
          isOpen ? 'scale-100 opacity-100' : 'scale-0 opacity-0'
        }`}
      >
        {/* Header */}
        <div className="bg-gradient-to-r from-blue-600 to-indigo-600 p-4 flex justify-between items-center text-white">
          <div className="flex items-center gap-2">
            <Bot size={20} />
            <h3 className="font-bold text-sm">Recruiter Assistant ✨</h3>
          </div>
          <button onClick={() => setIsOpen(false)} className="hover:bg-white/20 rounded p-1 transition">
            <X size={16} />
          </button>
        </div>

        {/* Tabs */}
        <div className="flex border-b border-gray-200 dark:border-gray-700">
          <button 
            onClick={() => { setActiveTab('chat'); setMessages([{ role: 'ai', text: "Hi! Ask me anything about Vigneshwaran's skills." }]); }}
            className={`flex-1 py-3 text-sm font-medium flex justify-center items-center gap-2 ${activeTab === 'chat' ? 'text-blue-600 bg-blue-50 dark:bg-gray-700 dark:text-blue-400' : 'text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700'}`}
          >
            <MessageSquare size={14} /> Chat
          </button>
          <button 
            onClick={() => { setActiveTab('match'); setMessages([{ role: 'ai', text: "Paste a Job Description (JD) below, and I'll tell you why Vigneshwaran is a good fit!" }]); }}
            className={`flex-1 py-3 text-sm font-medium flex justify-center items-center gap-2 ${activeTab === 'match' ? 'text-blue-600 bg-blue-50 dark:bg-gray-700 dark:text-blue-400' : 'text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-700'}`}
          >
            <Briefcase size={14} /> Job Match
          </button>
        </div>

        {/* Content Area */}
        <div className="h-80 overflow-y-auto p-4 bg-gray-50 dark:bg-gray-900/50 space-y-3">
          {messages.map((msg, idx) => (
            <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div 
                className={`max-w-[85%] rounded-lg p-3 text-sm ${
                  msg.role === 'user' 
                    ? 'bg-blue-600 text-white' 
                    : 'bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-200 shadow-sm border border-gray-100 dark:border-gray-600'
                }`}
              >
                {/* Basic Markdown-ish rendering for bullet points */}
                {msg.text.split('\\n').map((line, i) => (
                  <p key={i} className={line.trim().startsWith('*') || line.trim().startsWith('-') || line.match(/^\d\./) ? 'ml-2 mb-1' : 'mb-1'}>
                    {line}
                  </p>
                ))}
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-white dark:bg-gray-700 rounded-lg p-3 shadow-sm border border-gray-100 dark:border-gray-600">
                <Loader2 className="animate-spin text-blue-600" size={16} />
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Area */}
        <div className="p-3 bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700 flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
            placeholder={activeTab === 'chat' ? "Ask about skills..." : "Paste Job Description..."}
            className="flex-1 bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-white rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button 
            onClick={handleSend}
            disabled={isLoading || !input.trim()}
            className="bg-blue-600 text-white p-2 rounded-lg hover:bg-blue-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <Send size={18} />
          </button>
        </div>
      </div>

      {/* Toggle Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="pointer-events-auto bg-blue-600 hover:bg-blue-700 text-white p-4 rounded-full shadow-lg hover:shadow-xl transition-all duration-300 group flex items-center gap-2"
      >
        <Sparkles className="animate-pulse" size={24} />
        <span className="max-w-0 overflow-hidden group-hover:max-w-xs transition-all duration-300 whitespace-nowrap font-medium">
          Ask AI
        </span>
      </button>
    </div>
  );
};

// --- Components ---

const SectionTitle = ({ children, subtitle }) => (
  <div className="mb-12 text-center">
    <h2 className="text-3xl font-bold text-gray-900 dark:text-white sm:text-4xl mb-3">
      {children}
    </h2>
    {subtitle && <p className="text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">{subtitle}</p>}
    <div className="w-16 h-1 bg-blue-600 mx-auto mt-4 rounded-full"></div>
  </div>
);

const Card = ({ children, className = "" }) => (
  <div className={`bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 hover:shadow-xl transition-all duration-300 border border-gray-100 dark:border-gray-700 ${className}`}>
    {children}
  </div>
);

const Badge = ({ children, color = "blue" }) => {
  const colors = {
    blue: "bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200",
    green: "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
    purple: "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200",
  };
  return (
    <span className={`px-3 py-1 rounded-full text-xs font-semibold ${colors[color] || colors.blue}`}>
      {children}
    </span>
  );
};

// --- Main Application ---

export default function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [activeSection, setActiveSection] = useState('home');

  // Handle Dark Mode
  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  // Scroll Spy
  useEffect(() => {
    const handleScroll = () => {
      const sections = ['home', 'about', 'skills', 'projects', 'experience', 'contact'];
      const scrollPosition = window.scrollY + 100;

      for (const section of sections) {
        const element = document.getElementById(section);
        if (element && element.offsetTop <= scrollPosition && (element.offsetTop + element.offsetHeight) > scrollPosition) {
          setActiveSection(section);
        }
      }
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'Home', href: '#home' },
    { name: 'About', href: '#about' },
    { name: 'Skills', href: '#skills' },
    { name: 'Projects', href: '#projects' },
    { name: 'Experience', href: '#experience' },
    { name: 'Contact', href: '#contact' },
  ];

  return (
    <div className={`min-h-screen font-sans transition-colors duration-300 ${darkMode ? 'dark:bg-gray-900 dark:text-gray-100' : 'bg-gray-50 text-gray-900'}`}>
      
      {/* Navigation */}
      <nav className="fixed w-full z-40 bg-white/90 dark:bg-gray-900/90 backdrop-blur-sm border-b border-gray-200 dark:border-gray-800 transition-colors duration-300">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex-shrink-0 flex items-center">
              <span className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-600">
                VS
              </span>
            </div>
            
            {/* Desktop Menu */}
            <div className="hidden md:flex items-center space-x-8">
              {navLinks.map((link) => (
                <a
                  key={link.name}
                  href={link.href}
                  className={`text-sm font-medium transition-colors hover:text-blue-600 ${activeSection === link.href.substring(1) ? 'text-blue-600' : 'text-gray-600 dark:text-gray-300'}`}
                >
                  {link.name}
                </a>
              ))}
              <button
                onClick={() => setDarkMode(!darkMode)}
                className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
                aria-label="Toggle Dark Mode"
              >
                {darkMode ? <Sun size={20} className="text-yellow-400" /> : <Moon size={20} className="text-gray-600" />}
              </button>
              <a
                href={personalInfo.resumeLink}
                className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 transition-colors shadow-md hover:shadow-lg"
              >
                Resume
              </a>
            </div>

            {/* Mobile Menu Button */}
            <div className="flex items-center md:hidden gap-4">
              <button
                onClick={() => setDarkMode(!darkMode)}
                className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800"
              >
                {darkMode ? <Sun size={20} className="text-yellow-400" /> : <Moon size={20} className="text-gray-600" />}
              </button>
              <button
                onClick={() => setIsMenuOpen(!isMenuOpen)}
                className="p-2 rounded-md text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800"
              >
                {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
              </button>
            </div>
          </div>
        </div>

        {/* Mobile Dropdown */}
        {isMenuOpen && (
          <div className="md:hidden bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800">
            <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
              {navLinks.map((link) => (
                <a
                  key={link.name}
                  href={link.href}
                  onClick={() => setIsMenuOpen(false)}
                  className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 dark:text-gray-200 hover:bg-blue-50 dark:hover:bg-gray-800 hover:text-blue-600"
                >
                  {link.name}
                </a>
              ))}
              <a
                href={personalInfo.resumeLink}
                className="block w-full text-center mt-4 px-4 py-3 bg-blue-600 text-white rounded-md font-medium"
              >
                Download Resume
              </a>
            </div>
          </div>
        )}
      </nav>

      {/* Hero Section */}
      <section id="home" className="pt-32 pb-16 md:pt-48 md:pb-32 px-4 bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-gray-900 dark:to-gray-800 transition-colors duration-300">
        <div className="max-w-7xl mx-auto text-center">
          <div className="inline-block p-1 px-3 rounded-full bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-300 mb-6 text-sm font-semibold tracking-wide">
            Open to Work: Immediate Joiner
          </div>
          <h1 className="text-4xl md:text-6xl font-extrabold text-gray-900 dark:text-white mb-6 tracking-tight">
            Hi, I'm {personalInfo.name} <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">
              {personalInfo.role}
            </span>
          </h1>
          <p className="mt-4 max-w-2xl mx-auto text-xl text-gray-600 dark:text-gray-300 leading-relaxed">
            {personalInfo.tagline}
          </p>
          <div className="mt-10 flex justify-center gap-4 flex-col sm:flex-row">
            <a
              href="#projects"
              className="px-8 py-3.5 border border-transparent text-base font-semibold rounded-lg text-white bg-blue-600 hover:bg-blue-700 md:text-lg transition-all shadow-lg hover:shadow-blue-500/30"
            >
              View Projects
            </a>
            <a
              href={personalInfo.resumeLink}
              className="px-8 py-3.5 border border-gray-300 dark:border-gray-600 text-base font-semibold rounded-lg text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-800 hover:bg-gray-50 dark:hover:bg-gray-700 md:text-lg transition-all shadow-sm hover:shadow-md flex items-center justify-center gap-2"
            >
              <FileText size={20} /> Download CV
            </a>
          </div>
          
          <div className="mt-16 animate-bounce text-gray-400">
             <ChevronDown className="mx-auto" size={32} />
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="py-20 bg-white dark:bg-gray-900">
        <div className="max-w-4xl mx-auto px-4 sm:px-6">
          <SectionTitle subtitle="Passionate about secure, scalable code.">About Me</SectionTitle>
          <div className="prose prose-lg mx-auto text-center text-gray-600 dark:text-gray-300">
            <p>{personalInfo.summary}</p>
          </div>
          <div className="mt-12 grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
             {[
               { icon: <Code size={32} />, label: "Web Dev" },
               { icon: <Shield size={32} />, label: "Security" },
               { icon: <Database size={32} />, label: "Backend" },
               { icon: <Terminal size={32} />, label: "Automation" }
             ].map((item, i) => (
               <div key={i} className="p-4 rounded-lg bg-gray-50 dark:bg-gray-800 hover:bg-blue-50 dark:hover:bg-blue-900/20 transition-colors">
                 <div className="text-blue-600 dark:text-blue-400 flex justify-center mb-2">{item.icon}</div>
                 <span className="font-medium">{item.label}</span>
               </div>
             ))}
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section id="skills" className="py-20 bg-gray-50 dark:bg-gray-800/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6">
          <SectionTitle subtitle="My technical toolbox">Technical Skills</SectionTitle>
          
          <div className="grid md:grid-cols-2 gap-12">
            {/* Left Col: Languages & Frameworks */}
            <div className="space-y-8">
              <Card>
                <h3 className="text-xl font-bold mb-6 flex items-center gap-2">
                  <Code className="text-blue-600" /> Languages
                </h3>
                <div className="space-y-4">
                  {skills.languages.map((skill) => (
                    <div key={skill.name}>
                      <div className="flex justify-between mb-1">
                        <span className="font-medium text-gray-700 dark:text-gray-300">{skill.name}</span>
                        <span className="text-sm text-gray-500">{skill.level}%</span>
                      </div>
                      <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2.5">
                        <div className="bg-blue-600 h-2.5 rounded-full" style={{ width: `${skill.level}%` }}></div>
                      </div>
                    </div>
                  ))}
                </div>
              </Card>

              <Card>
                <h3 className="text-xl font-bold mb-6 flex items-center gap-2">
                  <Server className="text-purple-600" /> Frameworks
                </h3>
                <div className="flex flex-wrap gap-2">
                  {skills.frameworks.map((fw) => (
                    <span key={fw.name} className="px-4 py-2 bg-purple-50 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 rounded-lg font-medium text-sm border border-purple-100 dark:border-purple-800">
                      {fw.name}
                    </span>
                  ))}
                </div>
              </Card>
            </div>

            {/* Right Col: Tools & Core Concepts */}
            <div className="space-y-8">
              <Card>
                <h3 className="text-xl font-bold mb-6 flex items-center gap-2">
                  <Terminal className="text-green-600" /> Tools & Platforms
                </h3>
                <div className="grid grid-cols-2 gap-4">
                  {skills.tools.map((tool) => (
                    <div key={tool.name} className="flex items-center gap-3 p-3 rounded-lg bg-gray-50 dark:bg-gray-700/50 border border-gray-100 dark:border-gray-700">
                      <span className="text-gray-600 dark:text-gray-400">{tool.icon}</span>
                      <span className="font-medium text-gray-800 dark:text-gray-200">{tool.name}</span>
                    </div>
                  ))}
                </div>
              </Card>

              <Card>
                <h3 className="text-xl font-bold mb-6 flex items-center gap-2">
                  <Shield className="text-indigo-600" /> Core Concepts
                </h3>
                <div className="flex flex-wrap gap-2">
                  {skills.core.map((concept) => (
                    <span key={concept} className="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-full text-sm">
                      {concept}
                    </span>
                  ))}
                </div>
              </Card>
            </div>
          </div>
        </div>
      </section>

      {/* Projects Section - The Star of the Show */}
      <section id="projects" className="py-20 bg-white dark:bg-gray-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6">
          <SectionTitle subtitle="Real-world problems solved with code">Featured Projects</SectionTitle>
          
          <div className="grid lg:grid-cols-3 md:grid-cols-2 gap-8">
            {projects.map((project, index) => (
              <Card key={index} className="flex flex-col h-full hover:scale-[1.02] transition-transform">
                <div className="p-2">
                  <div className="flex justify-between items-start mb-4">
                    <Badge color="blue">{project.category}</Badge>
                    <div className="flex gap-2">
                      <a href={project.links.github} className="text-gray-500 hover:text-gray-900 dark:hover:text-white" title="View Code">
                        <Github size={20} />
                      </a>
                      <a href={project.links.demo} className="text-gray-500 hover:text-gray-900 dark:hover:text-white" title="Live Demo">
                        <ExternalLink size={20} />
                      </a>
                    </div>
                  </div>
                  <h3 className="text-xl font-bold mb-3 text-gray-900 dark:text-white">{project.title}</h3>
                  
                  <div className="space-y-4 mb-6 flex-grow">
                    <div>
                      <h4 className="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1">The Problem</h4>
                      <p className="text-sm text-gray-600 dark:text-gray-300">{project.problem}</p>
                    </div>
                    <div>
                      <h4 className="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1">The Solution</h4>
                      <p className="text-sm text-gray-600 dark:text-gray-300">{project.solution}</p>
                    </div>
                    <div>
                      <h4 className="text-xs font-semibold text-green-600 dark:text-green-400 uppercase tracking-wider mb-1">Impact</h4>
                      <p className="text-sm text-gray-900 dark:text-gray-100 font-medium">{project.impact}</p>
                    </div>
                  </div>

                  <div className="pt-4 border-t border-gray-100 dark:border-gray-700 mt-auto">
                    <div className="flex flex-wrap gap-2">
                      {project.techStack.map((tech) => (
                        <span key={tech} className="text-xs font-mono bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-400 px-2 py-1 rounded">
                          {tech}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Experience Section */}
      <section id="experience" className="py-20 bg-gray-50 dark:bg-gray-800/50">
        <div className="max-w-4xl mx-auto px-4 sm:px-6">
          <SectionTitle subtitle="Professional history">Experience</SectionTitle>
          
          <div className="space-y-8 relative before:absolute before:inset-0 before:ml-5 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-gray-300 before:to-transparent">
            {experiences.map((exp, index) => (
              <div key={index} className="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                
                {/* Timeline Dot */}
                <div className="flex items-center justify-center w-10 h-10 rounded-full border-4 border-white dark:border-gray-900 bg-blue-500 shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10 text-white">
                  <Code size={16} />
                </div>
                
                {/* Card */}
                <div className="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white dark:bg-gray-800 p-6 rounded-xl shadow border border-gray-100 dark:border-gray-700">
                  <div className="flex justify-between items-center mb-2">
                    <h3 className="font-bold text-lg text-gray-900 dark:text-white">{exp.role}</h3>
                    <span className="text-xs font-semibold px-2 py-1 bg-blue-50 text-blue-600 rounded-full dark:bg-blue-900/30 dark:text-blue-300">{exp.period}</span>
                  </div>
                  <h4 className="text-blue-600 dark:text-blue-400 font-medium mb-3">{exp.company}</h4>
                  <p className="text-gray-600 dark:text-gray-300 text-sm mb-4 italic">{exp.description}</p>
                  <ul className="space-y-2">
                    {exp.achievements.map((item, i) => (
                      <li key={i} className="flex items-start text-sm text-gray-600 dark:text-gray-400">
                        <span className="mr-2 text-blue-500 mt-1">•</span>
                        {item}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Education & Certs */}
      <section className="py-20 bg-white dark:bg-gray-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6">
          <div className="grid md:grid-cols-2 gap-12">
            
            {/* Education */}
            <div>
              <h3 className="text-2xl font-bold mb-8 text-center flex justify-center items-center gap-2">
                <span className="bg-blue-100 dark:bg-blue-900 p-2 rounded-lg text-blue-600 dark:text-blue-300"><FileText size={24} /></span>
                Education
              </h3>
              <div className="space-y-6">
                {education.map((edu, index) => (
                  <div key={index} className="flex gap-4">
                    <div className="flex flex-col items-center">
                      <div className="w-3 h-3 bg-blue-600 rounded-full mt-2"></div>
                      <div className="w-0.5 h-full bg-gray-200 dark:bg-gray-700 mt-1"></div>
                    </div>
                    <div className="pb-6">
                      <h4 className="font-bold text-lg text-gray-900 dark:text-white">{edu.degree}</h4>
                      <p className="text-blue-600 dark:text-blue-400">{edu.institution}</p>
                      <div className="flex items-center gap-3 mt-1 text-sm text-gray-500">
                        <span>{edu.year}</span>
                        {edu.details && <span>• {edu.details}</span>}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Certifications */}
            <div>
              <h3 className="text-2xl font-bold mb-8 text-center flex justify-center items-center gap-2">
                <span className="bg-green-100 dark:bg-green-900 p-2 rounded-lg text-green-600 dark:text-green-300"><Shield size={24} /></span>
                Certifications
              </h3>
              <div className="grid gap-4">
                {certifications.map((cert, index) => (
                  <div key={index} className="flex items-center gap-3 p-4 bg-gray-50 dark:bg-gray-800 rounded-lg border border-gray-100 dark:border-gray-700 hover:shadow-md transition-shadow">
                    <div className="text-green-600 dark:text-green-400 flex-shrink-0">
                      <Shield size={20} />
                    </div>
                    <span className="font-medium text-gray-800 dark:text-gray-200">{cert}</span>
                  </div>
                ))}
              </div>
            </div>

          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-20 bg-blue-600 dark:bg-blue-900">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 text-center text-white">
          <h2 className="text-3xl font-bold mb-6">Let's Create Something Secure & Scalable</h2>
          <p className="mb-10 text-blue-100 text-lg">
            I'm currently available for full-time opportunities. <br/>
            Whether you have a question or just want to say hi, I'll try my best to get back to you!
          </p>
          
          <div className="bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-2xl text-gray-900 dark:text-white max-w-lg mx-auto">
            <div className="space-y-6">
              <a href={`mailto:${personalInfo.email}`} className="flex items-center gap-4 p-4 rounded-xl bg-gray-50 dark:bg-gray-700 hover:bg-blue-50 dark:hover:bg-blue-900/30 transition-colors group">
                <div className="bg-blue-100 dark:bg-blue-900 p-3 rounded-full text-blue-600 dark:text-blue-300 group-hover:scale-110 transition-transform">
                  <Mail size={24} />
                </div>
                <div className="text-left">
                  <p className="text-sm text-gray-500 dark:text-gray-400">Email Me</p>
                  <p className="font-semibold break-all">{personalInfo.email}</p>
                </div>
              </a>

              <a href={personalInfo.linkedin} target="_blank" rel="noopener noreferrer" className="flex items-center gap-4 p-4 rounded-xl bg-gray-50 dark:bg-gray-700 hover:bg-blue-50 dark:hover:bg-blue-900/30 transition-colors group">
                <div className="bg-blue-100 dark:bg-blue-900 p-3 rounded-full text-blue-600 dark:text-blue-300 group-hover:scale-110 transition-transform">
                  <Linkedin size={24} />
                </div>
                <div className="text-left">
                  <p className="text-sm text-gray-500 dark:text-gray-400">Connect on LinkedIn</p>
                  <p className="font-semibold">Vigneshwaran S</p>
                </div>
              </a>

              <div className="flex justify-center gap-6 mt-8 pt-6 border-t border-gray-100 dark:border-gray-700">
                <a href={personalInfo.github} className="text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors">
                  <Github size={28} />
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 bg-gray-50 dark:bg-gray-950 text-center text-gray-500 dark:text-gray-400 text-sm">
        <p>© {new Date().getFullYear()} {personalInfo.name}. All rights reserved.</p>
        <p className="mt-2">Built with React & Tailwind CSS</p>
      </footer>
      
      {/* Recruiter AI Assistant Widget */}
      <RecruiterAI />

    </div>
  );
}
"""
}

# Create directories
if not os.path.exists(project_name):
    os.makedirs(project_name)

src_path = os.path.join(project_name, "src")
if not os.path.exists(src_path):
    os.makedirs(src_path)

# Write files
for filename, content in files.items():
    file_path = os.path.join(project_name, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
        # Append a newline for good measure
        f.write("\n")

print(f"Project '{project_name}' has been successfully generated!")
print(f"Instructions:")
print(f"1. cd {project_name}")
print(f"2. npm install")
print(f"3. npm run dev")