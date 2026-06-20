================================================
FILE: README.md
================================================
# Luminary AI

Luminary AI is an AI-as-a-service platform aimed at empowering small and mid-sized businesses with AI-driven solutions. The project includes a frontend built with Next.js and a backend powered by FastAPI.

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Frontend Setup

1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```

The frontend should now be running on `http://localhost:3000`.

### Backend (AI Services) Setup

1. Navigate to the backend directory (assuming it's named `ml`):
   ```sh
   cd ml
   ```
2. (Optional) Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Add your Groq API Key:
   - Go to [https://console.groq.com/keys](https://console.groq.com/keys)
   - Log in or sign up
   - Generate an API Key
   - Store it in `/ml/.env` by creating a `.env` file and adding:
     ```
     GROQ_API_KEY=your_generated_key
     ```
   - Or export it in your terminal:
     ```sh
     export GROQ_API_KEY=your_generated_key
     ```
5. Start the FastAPI server:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

The backend should now be running on `http://localhost:8000`.

## Features
- **Competitor Analysis & SWOT Insights**
- **AI-powered Branding (Name, Logo, Tagline Generation)**
- **Domain-specific Chatbots**
- **SEO Optimization for Digital Growth**
- **Pretrained Models & Custom AI Solutions**

## Contributing
Feel free to fork this repository and create pull requests to contribute!

## License
This project is licensed under the MIT License.




================================================
FILE: frontend/README.md
================================================
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.



================================================
FILE: frontend/components.json
================================================
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "src/app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}


================================================
FILE: frontend/eslint.config.mjs
================================================
import { dirname } from "path";
import { fileURLToPath } from "url";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

const eslintConfig = [
  ...compat.extends("next/core-web-vitals", "next/typescript"),
];

export default eslintConfig;



================================================
FILE: frontend/next.config.ts
================================================
// next.config.js
const nextConfig = {
  images: {
    domains: [
      "weybee.com",
      "futureprooftech.com",
      "digitalclicks.ae",
      "assets.nflxext.com",
      "spycloud.com",
      "www.upwork.com",
    ],
  },
};

module.exports = nextConfig;


================================================
FILE: frontend/package.json
================================================
{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@radix-ui/react-label": "^2.1.1",
    "@radix-ui/react-scroll-area": "^1.2.2",
    "@radix-ui/react-slot": "^1.1.1",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "firebase": "^11.2.0",
    "framer-motion": "^12.0.6",
    "handlebars": "^4.7.8",
    "lucide-react": "^0.474.0",
    "next": "15.1.6",
    "nodemailer": "^6.10.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-loading-skeleton": "^3.5.0",
    "react-markdown": "^9.0.3",
    "react-router-dom": "^7.1.5",
    "tailwind-merge": "^3.0.1",
    "tailwindcss-animate": "^1.0.7"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3",
    "@shadcn/ui": "^0.0.4",
    "@types/node": "^20",
    "@types/nodemailer": "^6.4.17",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "eslint": "^9",
    "eslint-config-next": "15.1.6",
    "postcss": "^8",
    "tailwindcss": "^3.4.1",
    "typescript": "^5"
  }
}



================================================
FILE: frontend/postcss.config.mjs
================================================
/** @type {import('postcss-load-config').Config} */
const config = {
  plugins: {
    tailwindcss: {},
  },
};

export default config;



================================================
FILE: frontend/tailwind.config.ts
================================================
import type { Config } from "tailwindcss";

export default {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "var(--primary)",
          foreground: "var(--primary-foreground)",
        },
        secondary: {
          DEFAULT: "var(--secondary)",
          foreground: "var(--secondary-foreground)",
        },
        background: {
          DEFAULT: "var(--background)",
          secondary: "var(--background-secondary)",
        },
        border: "var(--border)",
        muted: {
          DEFAULT: "var(--muted)",
          foreground: "var(--muted-foreground)",
        },
        accent: {
          DEFAULT: "var(--accent)",
          foreground: "var(--accent-foreground)",
        },
        level: {
          1: "#f9f3ec",
          2: "#f97315",
          3: "#262b33"
        }
      },
    },
  },
  plugins: [
    function({ addBase }: { addBase: (base: Record<string, any>) => void }) {
      addBase({
        ":root": {
          "--primary": "#000000",
          "--primary-foreground": "#ffffff",
          "--secondary": "#f1f5f9",
          "--secondary-foreground": "#0f172a",
          "--background": "#ffffff", 
          "--background-secondary": "#f8fafc",
          "--border": "#e2e8f0",
          "--muted": "#f1f5f9",
          "--muted-foreground": "#64748b",
          "--accent": "#f1f5f9",
          "--accent-foreground": "#0f172a"
        }
      });
    }
  ],
} satisfies Config;


================================================
FILE: frontend/tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}



================================================
FILE: frontend/src/app/globals.css
================================================
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  font-family: Arial, Helvetica, sans-serif;
}

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 0 0% 3.9%;
    --card: 0 0% 100%;
    --card-foreground: 0 0% 3.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 0 0% 3.9%;
    --primary: 0 0% 9%;
    --primary-foreground: 0 0% 98%;
    --secondary: 0 0% 96.1%;
    --secondary-foreground: 0 0% 9%;
    --muted: 0 0% 96.1%;
    --muted-foreground: 0 0% 45.1%;
    --accent: 0 0% 96.1%;
    --accent-foreground: 0 0% 9%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 0 0% 98%;
    --border: 0 0% 89.8%;
    --input: 0 0% 89.8%;
    --ring: 0 0% 3.9%;
    --chart-1: 12 76% 61%;
    --chart-2: 173 58% 39%;
    --chart-3: 197 37% 24%;
    --chart-4: 43 74% 66%;
    --chart-5: 27 87% 67%;
    --radius: 0.5rem;
  }
  .dark {
    --background: 0 0% 3.9%;
    --foreground: 0 0% 98%;
    --card: 0 0% 3.9%;
    --card-foreground: 0 0% 98%;
    --popover: 0 0% 3.9%;
    --popover-foreground: 0 0% 98%;
    --primary: 0 0% 98%;
    --primary-foreground: 0 0% 9%;
    --secondary: 0 0% 14.9%;
    --secondary-foreground: 0 0% 98%;
    --muted: 0 0% 14.9%;
    --muted-foreground: 0 0% 63.9%;
    --accent: 0 0% 14.9%;
    --accent-foreground: 0 0% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 0 0% 98%;
    --border: 0 0% 14.9%;
    --input: 0 0% 14.9%;
    --ring: 0 0% 83.1%;
    --chart-1: 220 70% 50%;
    --chart-2: 160 60% 45%;
    --chart-3: 30 80% 55%;
    --chart-4: 280 65% 60%;
    --chart-5: 340 75% 55%;
  }
}



================================================
FILE: frontend/src/app/layout.tsx
================================================
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Luminary AI",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}



================================================
FILE: frontend/src/app/page.tsx
================================================
import Footer from "@/components/Footer";
import Hero from "@/components/Hero";
import Navbar from "@/components/Navbar";
import Work from "@/components/Work";
import BrandLogos from "@/components/Sponsors";

export default function Home() {
  return (
    <div className="bg-level-1">
      <Navbar />
      <Hero />
      <Work />
      <BrandLogos />
      <Footer />
    </div>
  );
}


================================================
FILE: frontend/src/app/chat/page.tsx
================================================
import ChatPage from '@/components/Chatbot'
import Navbar from '@/components/Navbar'
import React from 'react'

const page = () => {
  return (
    <div>
        <Navbar />
      <ChatPage />
    </div>
  )
}

export default page



================================================
FILE: frontend/src/app/contact/page.tsx
================================================
'use client'
import Contact from '@/components/ContactUs'
import Footer from '@/components/Footer'
import Navbar from '@/components/Navbar'
import React from 'react'

const page = () => {
  return (
    <div className=''>
      <Navbar />
      <Contact />
      <Footer />
    </div>
  )
}

export default page



================================================
FILE: frontend/src/app/explore/page.tsx
================================================
import Chatbot from '@/components/ChatbotSmall'
import CompanyInput from '@/components/CompanyInput'
import Navbar from '@/components/Navbar'
import React from 'react'

const page = () => {
  return (
    <div className='items-center justify-center'>
    <Navbar />
      <CompanyInput />
      <Chatbot />
    </div>
  )
}

export default page



================================================
FILE: frontend/src/app/sectors/page.tsx
================================================
import AgentRow from '@/components/ChatbotCard'
import Navbar from '@/components/Navbar'
import React from 'react'

const page = () => {
  return (
    <div>
        <Navbar />
      <AgentRow />
    </div>
  )
}

export default page



================================================
FILE: frontend/src/app/signin/page.tsx
================================================
import SignIn from '@/components/Signin'
import React from 'react'

const page = () => {
  return (
    <div>
      <SignIn />
    </div>
  )
}

export default page



================================================
FILE: frontend/src/app/signup/page.tsx
================================================
import SignUp from '@/components/Signup'
import React from 'react'

const page = () => {
  return (
    <div>
      <SignUp />
    </div>
  )
}

export default page



================================================
FILE: frontend/src/app/sponsors/page.tsx
================================================
import BrandLogos from '@/components/Sponsors'
import React from 'react'

const page = () => {
  return (
    <div>
      <BrandLogos />
    </div>
  )
}

export default page



================================================
FILE: frontend/src/app/team/page.tsx
================================================
import React from 'react'
import Team from '@/components/Team'


const page = () => {
  return (
    <div className='bg-level-1'>
     <Team />
    </div>

  )
}

export default page



================================================
FILE: frontend/src/app/test/page.tsx
================================================
import AgentCard from '@/components/ChatbotCard'
import React from 'react'

const page = () => {
  return (
    <div>
      <AgentCard />
    </div>
  )
}

export default page



================================================
FILE: frontend/src/components/Analysis.tsx
================================================
'use client';
import { useState } from "react";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Building2, MapPin, Briefcase, BarChart2, ArrowLeft } from "lucide-react";
import { Alert, AlertDescription } from "@/components/ui/alert";

interface CompanyData {
  company: {
    official_name: string;
    industry_type: string;
    headquarters: string;
    key_products_services: string[];
    website: string;
  };
  competitors: {
    name: string;
    industry_type: string;
    headquarters: string;
    key_products_services: string[];
  }[];
}

interface SWOTSection {
    "Official Name": string;
    "Strengths of Company": string;
    "Weakness of Company": string;
    "Opportunity of Company": string;
    "Threats to the Company": string;
  }

  
  interface SWOTData {
    companies: SWOTSection[];
  }

const CompetitorCards = ({ competitors }: { competitors: CompanyData["competitors"] }) => (
  <div className="lg:w-2/3 w-full animate-slide-in-right">
    <div className="flex flex-col">
      <div className="grid md:grid-cols-2 gap-6 flex-grow">
        {competitors.slice(0, 4).map((competitor, index) => {
          const isLevel2 = index % 1 === 0;

          return (
            <Card
              key={index}
              className={`transform hover:scale-102 transition-all duration-300 shadow-lg animate-fade-in ${
                isLevel2
                  ? "bg-gradient-to-br from-orange-50 to-orange-100 hover:shadow-orange-200"
                  : "bg-gradient-to-br from-gray-900 to-black hover:shadow-gray-800"
              }`}
              style={{
                animationDelay: `${index * 150}ms`
              }}
            >
              <CardHeader className="p-4">
                <CardTitle className={`text-xl font-bold flex items-center gap-3 ${
                  isLevel2 ? "text-orange-800" : "text-white"
                }`}>
                  <Building2 className={isLevel2 ? "text-orange-500" : "text-white"} />
                  {competitor.name}
                </CardTitle>
              </CardHeader>
              <CardContent className="">
                <div className="space-y-4">
                  <div className="group">
                    <h3 className={`font-semibold text-lg mb-1 ${
                      isLevel2 ? "text-orange-800" : "text-gray-200"
                    }`}>
                      Industry Type
                    </h3>
                    <p className={`transform group-hover:translate-x-2 transition-transform ${
                      isLevel2 ? "text-orange-700" : "text-gray-300"
                    }`}>
                      {competitor.industry_type}
                    </p>
                  </div>
                  <div className="group">
                    <h3 className={`font-semibold text-lg mb-1 ${
                      isLevel2 ? "text-orange-800" : "text-gray-200"
                    }`}>
                      Headquarters
                    </h3>
                    <p className={`transform group-hover:translate-x-2 transition-transform ${
                      isLevel2 ? "text-orange-700" : "text-gray-300"
                    }`}>
                      {competitor.headquarters}
                    </p>
                  </div>
                  <div>
                    <h3 className={`font-semibold text-lg mb-1 ${
                      isLevel2 ? "text-orange-800" : "text-gray-200"
                    }`}>
                      Key Products & Services
                    </h3>
                    <ul className="space-y-2">
                      {competitor.key_products_services.map((service, serviceIndex) => (
                        <li key={serviceIndex} className={`flex items-center gap-2 group ${
                          isLevel2 ? "text-orange-700" : "text-gray-300"
                        }`}>
                          <div className={`w-1.5 h-1.5 rounded-full ${
                            isLevel2 ? "bg-orange-500" : "bg-white"
                          }`}></div>
                          <span className="transform group-hover:translate-x-2 transition-transform">
                            {service}
                          </span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </CardContent>
            </Card>
          );
        })}
      </div>
    </div>
  </div>
);

export default function CompanyInfoDisplay({ companyData }: { companyData: CompanyData }) {
  const [showSWOT, setShowSWOT] = useState(false);
  const [swotData, setSwotData] = useState<SWOTData | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  // Handle SWOT analysis button click
  const handleSWOTClick = async () => {
    setIsLoading(true);
    try {
        companyData.competitors.pop();
        companyData.competitors.pop();
      // Send a POST request to the SWOT analysis endpoint
      const response = await fetch("https://dotslash-backend.onrender.com/companies-analysis", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(companyData), // Send the company data as the request body
      });

      if (!response.ok) {
        console.log(companyData);
        
        throw new Error("Failed to fetch SWOT analysis");
      }

      const data: SWOTData = await response.json();
      setSwotData(data); // Update the SWOT data state
      console.log(data);
      
      setShowSWOT(true); // Show the SWOT analysis component
    } catch (error) {
      console.error("Error fetching SWOT analysis:", error);
    } finally {
      setIsLoading(false);
    }
  };
  console.log(companyData);
  // Check if industry is available
  if (!companyData.company.industry_type) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 p-8">
        <div className="max-w-7xl mx-auto">
          <Alert className="bg-red-50 text-red-800 border-red-200">
            <AlertDescription>Company not found or industry data unavailable.</AlertDescription>
          </Alert>
        </div>
      </div>
    );
  }

  

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 p-8">
      <div className="max-w-7xl mx-auto">
        <div className="flex flex-col lg:flex-row gap-8 h-full">
          <div className="lg:w-1/3 w-full animate-slide-in-left h-full">
            <Card className="bg-white shadow-xl hover:shadow-2xl transition-all duration-300 h-full">
              <CardHeader className="bg-gradient-to-r from-gray-50 to-white p-6 border-b">
                <CardTitle className="text-3xl font-bold flex items-center gap-4">
                  <Building2 className="h-8 w-8 text-orange-500" />
                  {companyData.company.official_name}
                </CardTitle>
              </CardHeader>
              <CardContent className="p-6 h-full">
                <div className="grid gap-6 h-full">
                  <div className="flex items-start gap-4 group">
                    <Briefcase className="h-6 w-6 text-gray-700 mt-1 group-hover:text-orange-500 transition-colors" />
                    <div className="transform group-hover:translate-x-2 transition-transform">
                      <h3 className="font-semibold text-xl text-gray-900 mb-2">Industry Type</h3>
                      <p className="text-gray-600">{companyData.company.industry_type}</p>
                    </div>
                  </div>
                  <div className="flex items-start gap-4 group">
                    <MapPin className="h-6 w-6 text-gray-700 mt-1 group-hover:text-orange-500 transition-colors" />
                    <div className="transform group-hover:translate-x-2 transition-transform">
                      <h3 className="font-semibold text-xl text-gray-900 mb-2">Headquarters</h3>
                      <p className="text-gray-600">{companyData.company.headquarters}</p>
                    </div>
                  </div>
                  <div className="flex items-start gap-4 group flex-grow">
                    <Building2 className="h-6 w-6 text-gray-700 mt-1 group-hover:text-orange-500 transition-colors" />
                    <div className="transform group-hover:translate-x-2 transition-transform">
                      <h3 className="font-semibold text-xl text-gray-900 mb-2">Key Products & Services</h3>
                      <ul className="space-y-2 text-gray-600">
                        {companyData.company.key_products_services.map((service, index) => (
                          <li key={index} className="flex items-center gap-2 group/item">
                            <div className="w-2 h-2 bg-orange-500 rounded-full group-hover/item:scale-125 transition-transform"></div>
                            <span className="group-hover/item:translate-x-1 transition-transform">{service}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>

                  <button
                    onClick={handleSWOTClick}
                    disabled={isLoading}
                    className="mt-0 w-full group bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700 text-white rounded-lg px-4 py-3 transition-all duration-300 transform hover:-translate-y-0.5 hover:shadow-lg flex items-center justify-center gap-3"
                  >
                    {isLoading ? (
                      <>
                        <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                        <span className="font-semibold">Loading...</span>
                      </>
                    ) : showSWOT ? (
                      <>
                        <ArrowLeft className="w-6 h-6 transition-transform group-hover:scale-110 mr-2" />
                        <span className="font-semibold">Back to Competitors</span>
                      </>
                    ) : (
                      <>
                        <BarChart2 className="w-6 h-6 transition-transform group-hover:scale-110 mr-2" />
                        <span className="font-semibold">View SWOT Analysis</span>
                        <div className="ml-2 bg-white/20 rounded-full px-2 py-0.5 text-sm">
                          Get It Now
                        </div>
                      </>
                    )}
                  </button>
                </div>
              </CardContent>
            </Card>
          </div>

          {showSWOT && swotData ? (
            <div className="lg:w-2/3 w-full animate-slide-in-right">
            <div className="grid md:grid-cols-2 gap-6">
              {swotData.companies.map((section, index) => (
                <Card
                  key={index}
                  className={`transform hover:scale-105 transition-all duration-300 shadow-lg bg-gradient-to-br hover:shadow-xl`}
                  style={{ animationDelay: `${index * 150}ms` }}
                >
                  <CardHeader className="p-4">
                    <CardTitle className="text-xl font-bold flex items-center gap-3">
                      {section["Official Name"]}
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="p-4">
                    <ul className="space-y-3">
                      {Object.entries(section).map(([key, value], itemIndex) => (
                        key !== "Official Name" && (
                          <li key={itemIndex} className="flex items-center gap-2 group">
                            <div className="w-2 h-2 rounded-full bg-gray-500"></div>
                            <span className="transform group-hover:translate-x-2 transition-transform">
                              <strong>{key}:</strong> {value}
                            </span>
                          </li>
                        )
                      ))}
                    </ul>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
          ) : (
            <CompetitorCards competitors={companyData.competitors} />
          )}
        </div>
      </div>
    </div>
  );
}


================================================
FILE: frontend/src/components/Chatbot.tsx
================================================
"use client";

import React, { useState, useEffect, useCallback, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Send,
  User,
  Bot,
  Star,
  Moon,
  Heart,
  Infinity,
  RefreshCw,
  Copy,
  Check,
} from "lucide-react";
import ReactMarkdown from "react-markdown";

// Interfaces and Types
interface Message {
  id: string;
  text: string;
  type: "user" | "response";
  timestamp: Date;
}

interface QuickAction {
  id: string;
  icon: React.ElementType;
  text: string;
}

interface MarkdownComponentProps {
  children: React.ReactNode;
  [key: string] : unknown;
}

interface MessageBubbleProps {
  message: Message;
}

interface QuickActionsProps {
  onSelect: (actionText: string) => void;
}

// Custom Markdown Components
const MarkdownComponents: Record<string, React.FC<MarkdownComponentProps>> = {
  p: ({ children, ...props }) => (
    <p className="text-gray-800 leading-relaxed" {...props}>
      {children}
    </p>
  ),
  h1: ({ children, ...props }) => (
    <h1 className="text-2xl font-semibold text-gray-800 my-3" {...props}>
      {children}
    </h1>
  ),
  h2: ({ children, ...props }) => (
    <h2 className="text-xl font-semibold text-gray-800 my-2" {...props}>
      {children}
    </h2>
  ),
  h3: ({ children, ...props }) => (
    <h3 className="text-lg font-semibold text-gray-800 my-2" {...props}>
      {children}
    </h3>
  ),
  ul: ({ children, ...props }) => (
    <ul className="list-disc list-inside my-2 space-y-1" {...props}>
      {children}
    </ul>
  ),
  ol: ({ children, ...props }) => (
    <ol className="list-decimal list-inside my-2 space-y-1" {...props}>
      {children}
    </ol>
  ),
  li: ({ children, ...props }) => (
    <li className="text-gray-800" {...props}>
      {children}
    </li>
  ),
  code: ({ children, ...props }) => (
    <code className="bg-gray-100 rounded px-1 py-0.5 font-mono text-sm" {...props}>
      {children}
    </code>
  ),
  pre: ({ children, ...props }) => (
    <pre className="bg-gray-100 rounded-lg p-3 my-2 overflow-x-auto" {...props}>
      {children}
    </pre>
  ),
  blockquote: ({ children, ...props }) => (
    <blockquote className="border-l-4 border-gray-200 pl-4 my-2 italic" {...props}>
      {children}
    </blockquote>
  ),
};

const MessageBubble: React.FC<MessageBubbleProps> = ({ message }) => {
  const [isCopied, setIsCopied] = useState<boolean>(false);
  const isUser = message.type === "user";

  const handleCopy = () => {
    navigator.clipboard.writeText(message.text);
    setIsCopied(true);
    setTimeout(() => setIsCopied(false), 2000);
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className={`flex ${isUser ? "justify-end" : "justify-start"} mb-4`}
    >
      <div className={`flex gap-2 max-w-[80%] ${isUser ? "flex-row-reverse" : ""}`}>
        <div
          className={`w-8 h-8 rounded-full flex-shrink-0 flex items-center justify-center
            ${isUser ? "bg-orange-500" : "bg-gray-900"}`}
        >
          {isUser ? <User className="w-4 h-4 text-white" /> : <Bot className="w-4 h-4 text-white" />}
        </div>

        <div
          className={`group relative p-3 rounded-2xl
          ${isUser ? "bg-orange-500 text-white" : "bg-gray-100"}`}
        >
          <div className="prose prose-sm max-w-none">
            <ReactMarkdown components={MarkdownComponents}>{message.text}</ReactMarkdown>
          </div>
          <div className="flex items-center justify-between gap-4 mt-2">
            <span className="text-xs opacity-60">
              {message.timestamp.toLocaleTimeString([], {
                hour: "2-digit",
                minute: "2-digit",
              })}
            </span>
            {!isUser && (
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={handleCopy}
                className="opacity-0 group-hover:opacity-100 transition-opacity"
              >
                {isCopied ? (
                  <Check className="w-4 h-4 text-green-500" />
                ) : (
                  <Copy className="w-4 h-4 opacity-60" />
                )}
              </motion.button>
            )}
          </div>
        </div>
      </div>
    </motion.div>
  );
};

const TypingIndicator: React.FC = () => (
  <div className="flex items-center gap-2 mb-4">
    <div className="w-8 h-8 rounded-full bg-gray-900 flex items-center justify-center">
      <Bot className="w-4 h-4 text-white" />
    </div>
    <div className="px-4 py-2 rounded-2xl bg-gray-100">
      <div className="flex gap-1">
        {[0, 1, 2].map((dot) => (
          <motion.div
            key={dot}
            className="w-1.5 h-1.5 bg-gray-400 rounded-full"
            animate={{ y: [0, -3, 0] }}
            transition={{
              duration: 0.8,
              repeat: Infinity as unknown as number,
              delay: dot * 0.2,
            }}
          />
        ))}
      </div>
    </div>
  </div>
);

const QuickActions: React.FC<QuickActionsProps> = ({ onSelect }) => {
  const actions: QuickAction[] = [
    { id: "1", icon: Star, text: "Schedule Appointment" },
    { id: "2", icon: Moon, text: "Medication Reminder" },
    { id: "3", icon: Heart, text: "Symptom Checker" },
    { id: "4", icon: Infinity, text: "Find Doctor" },
  ];

  return (
    <div className="flex gap-2 overflow-x-auto py-2">
      {actions.map((action) => (
        <motion.button
          key={action.id}
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          onClick={() => onSelect(action.text)}
          className="flex items-center gap-2 px-4 py-2 bg-gray-100 rounded-full
            whitespace-nowrap hover:bg-gray-200 transition-colors"
        >
          <action.icon className="w-4 h-4" />
          <span className="text-sm">{action.text}</span>
        </motion.button>
      ))}
    </div>
  );
};

const ChatPage: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputMessage, setInputMessage] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    if (messages.length === 0) {
      setMessages([
        {
          id: "0",
          text: "Hi! I'm your AI assistant. How can I help you today?",
          type: "response",
          timestamp: new Date(),
        },
      ]);
    }
  }, [messages.length]);

  const sendMessage = useCallback(async () => {
    if (!inputMessage.trim() || isLoading) return;
  
    // Show the user's message immediately
    const userMessage: Message = {
      id: Date.now().toString(),
      text: inputMessage,
      type: "user",
      timestamp: new Date(),
    };
    setMessages((prev) => [...prev, userMessage]);
  
    try {
      setIsLoading(true);
      setError(null);
  
      // Send message to backend API and get response
      const response = await fetch("https://dotslash-backend.onrender.com/medical-bot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ msg: inputMessage }),
      });
  
      if (!response.ok) throw new Error("Failed to send message");
  
      const data = await response.json();
  
      // Immediately update the UI with the bot's response
      const botMessage: Message = {
        id: Date.now().toString(),
        text: data.response, // Using 'response' field directly
        type: "response",
        timestamp: new Date(),
      };
  
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      setError(err instanceof Error ? err.message : "An unknown error occurred.");
    } finally {
      setIsLoading(false);
      setInputMessage("");
    }
  }, [inputMessage, isLoading]);
  
  const handleQuickAction = (action: string) => {
    setInputMessage(action);
    sendMessage();
  };

  return (
    <div className="max-w-4xl mx-auto pt-24">
      <div className="space-y-4 ">
        {/* Main Chat Container */}
        <div className="bg-white rounded-2xl shadow-lg border-1 ">
          {/* Chat Header */}
          <div className="p-4 border-b ">
            <div className="flex items-center justify-between ">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-orange-500 rounded-full flex items-center justify-center">
                  <Bot className="w-5 h-5 text-white" />
                </div>
                <div>
                  <h2 className="font-semibold">Doc AI</h2>
                  <div className="flex items-center gap-2 text-sm text-gray-500">
                    <span className="flex items-center gap-1">
                      <span className="w-2 h-2 bg-green-500 rounded-full"></span>
                      Online
                    </span>
                  </div>
                </div>
              </div>
              <motion.button
                whileHover={{ scale: 1.05, rotate: 180 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => setMessages([])}
                className="p-2 hover:bg-gray-100 rounded-full"
              >
                <RefreshCw className="w-5 h-5" />
              </motion.button>
            </div>
          </div>

          {/* Chat Messages */}
          <div className="h-[500px] flex flex-col">
            <div className="flex-1 overflow-y-auto p-4">
              <AnimatePresence>
                {messages.map((message) => (
                  <MessageBubble key={message.id} message={message} />
                ))}
              </AnimatePresence>
              {isLoading && <TypingIndicator />}
              {error && (
                <div className="mb-4 p-4 text-sm text-red-600 bg-red-50 rounded-xl">
                  {error}
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>

            {/* Quick Actions */}
            <div className="p-4 border-t">
              <QuickActions onSelect={handleQuickAction} />
            </div>

            {/* Input Area */}
            <div className="p-4 border-t bg-white">
              <div className="flex gap-2">
                <input
                  type="text"
                  value={inputMessage}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                    setInputMessage(e.target.value)
                  }
                  onKeyPress={(e: React.KeyboardEvent) => {
                    if (e.key === "Enter" && !e.shiftKey) {
                      e.preventDefault();
                      sendMessage();
                    }
                  }}
                  placeholder="Type your message..."
                  className="flex-1 px-4 py-2 rounded-full bg-gray-100 focus:outline-none focus:ring-2 ring-orange-500
                    disabled:opacity-50 disabled:cursor-not-allowed"
                  disabled={isLoading}
                />
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  onClick={() => sendMessage()}
                  disabled={isLoading || !inputMessage.trim()}
                  className="px-6 py-2 bg-orange-500 text-white rounded-full
                    flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed
                    hover:bg-orange-600 transition-colors"
                >
                  <span className="hidden md:inline">Send</span>
                  <Send className="w-4 h-4" />
                </motion.button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatPage;



================================================
FILE: frontend/src/components/ChatbotCard.tsx
================================================
'use client'
import React, { useState } from 'react';
import { Card } from '@/components/ui/card';
import Link from 'next/link';
import Image from 'next/image';

interface Agent {
  title: string;
  subtitle: string;
  imagePath: string;
  isFirst?: boolean;
}

const agents: Agent[] = [
  {
    title: 'Healthcare Assistant',
    subtitle: 'Your AI-powered legal companion',
    imagePath: '/healthcare.png',
    isFirst: true
  },
  {
    title: 'AI Consultant',
    subtitle: 'Advanced AI solutions',
    imagePath: '/Legal.png'
  },
  {
    title: 'Business Advisor',
    subtitle: 'Strategic insights engine',
    imagePath: '/Ecommerce.png'
  },
  {
    title: 'Analytics Expert',
    subtitle: 'Data-driven decisions',
    imagePath: '/Finance.png'
  }
];

const AgentCard: React.FC<Agent & {
  isHovered: boolean;
  onMouseEnter: () => void;
  onMouseLeave: () => void;
}> = ({
  title,
  subtitle,
  imagePath,
  isFirst,
  isHovered,
  onMouseEnter,
  onMouseLeave
}) => {
    return (
      <div
        className="transform transition-all duration-300 ease-out"
        style={{
          transform: isHovered ? 'scale(1.05)' : 'scale(1)',
        }}
        onMouseEnter={onMouseEnter}
        onMouseLeave={onMouseLeave}
      >
        <Card
          className={`${isFirst ? 'w-80 h-[440px]' : 'w-72 h-[400px]'} bg-white rounded-xl p-6 hover:shadow-2xl transition-shadow relative`}
        >
          <div className="w-full h-1/2 mb-4">
            <Image
              src={imagePath}
              alt={title}
              height={160}
              width={160}
              className="w-full h-full object-cover rounded-xl"></Image>
          </div>

          <div className="space-y-2">
            <h2 className="text-xl font-bold text-gray-900">{title}</h2>
            <p className="text-sm text-gray-600">{subtitle}</p>
          </div>

          <div className="absolute bottom-6 left-6 right-6">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center space-x-2">
                <span className="text-amber-500 font-bold">O</span>
                <span className="text-gray-600">Olama</span>
              </div>

              <div className="flex space-x-2">
                <button className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center hover:bg-blue-700 transition-colors">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z" />
                    <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
                    <line x1="12" y1="19" x2="12" y2="23" />
                    <line x1="8" y1="23" x2="16" y2="23" />
                  </svg>
                </button>
                <button className="w-8 h-8 bg-red-600 rounded-full flex items-center justify-center hover:bg-red-700 transition-colors">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8" />
                    <polyline points="16 6 12 2 8 6" />
                    <line x1="12" y1="2" x2="12" y2="15" />
                  </svg>
                </button>
              </div>
            </div>

            {isFirst ? (
              <Link href="/chat">
              <button className="w-full py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium">
                Try Now
              </button>
              </Link>
            ) : (
              <button className="w-full py-2 bg-gray-300 text-gray-500 rounded-lg cursor-not-allowed font-medium">
                Coming Soon
              </button>
            )}
          </div>
        </Card>
      </div>
    );
  };

const AgentRow: React.FC = () => {
  const [hoveredIndex, setHoveredIndex] = useState<number | null>(null);

  return (
    <div className="w-full pt-32">
      <div className="flex justify-between items-center max-w-7xl mx-auto gap-6">
        {agents.map((agent, index) => (
          <AgentCard
            key={index}
            {...agent}
            isHovered={hoveredIndex === index}
            onMouseEnter={() => setHoveredIndex(index)}
            onMouseLeave={() => setHoveredIndex(null)}
          />
        ))}
      </div>
    </div>
  );
};

export default AgentRow;


================================================
FILE: frontend/src/components/ChatbotSmall.tsx
================================================
"use client"
import { useState, useEffect, useRef } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import { MessageCircle, Send, X, Bot, User } from 'lucide-react'
import { Button as BaseButton, ButtonProps as BaseButtonProps } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { ScrollArea } from "@/components/ui/scroll-area"

type Message = {
  id: number;
  content: string;
  role: 'user' | 'bot';
}

type ButtonProps = BaseButtonProps & {
  variant?: 'default' | 'destructive' | 'outline' | 'secondary' | 'ghost' | 'link';
  size?: 'default' | 'sm' | 'lg' | 'icon';
};

const Button = ({ variant, size, ...props }: ButtonProps) => (
  <BaseButton {...props} className={`${props.className} ${variant} ${size}`} />
);

// Typing animation component
const TypingIndicator = () => (
  <div className="flex space-x-2 p-3 bg-orange-100 rounded-lg items-center">
    <Bot className="w-5 h-5 text-orange-500" />
    <div className="flex space-x-1">
      <motion.div
        className="w-2 h-2 bg-orange-400 rounded-full"
        animate={{ y: [0, -5, 0] }}
        transition={{ duration: 0.5, repeat: Infinity, repeatType: "reverse" }}
      />
      <motion.div
        className="w-2 h-2 bg-orange-400 rounded-full"
        animate={{ y: [0, -5, 0] }}
        transition={{ duration: 0.5, repeat: Infinity, repeatType: "reverse", delay: 0.2 }}
      />
      <motion.div
        className="w-2 h-2 bg-orange-400 rounded-full"
        animate={{ y: [0, -5, 0] }}
        transition={{ duration: 0.5, repeat: Infinity, repeatType: "reverse", delay: 0.4 }}
      />
    </div>
  </div>
);

// Message component
const ChatMessage = ({ message }: { message: Message }) => {
  const isUser = message.role === 'user';
  
  return (
    <div className={`mb-4 ${isUser ? 'text-right' : 'text-left'}`}>
      <div className={`flex items-center gap-2 mb-1 ${isUser ? 'justify-end' : 'justify-start'}`}>
        {!isUser && <Bot className="w-4 h-4 text-orange-500" />}
        <span className="text-sm text-orange-500">
          {isUser ? 'You' : 'Bot'}
        </span>
        {isUser && <User className="w-4 h-4 text-orange-500" />}
      </div>
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3 }}
      >
        <span
          className={`inline-block p-3 rounded-lg ${
            isUser
              ? 'bg-orange-500 text-white rounded-tr-none'
              : 'bg-orange-100 text-orange-800 rounded-tl-none'
          }`}
        >
          {message.content}
        </span>
      </motion.div>
    </div>
  );
};

export default function Chatbot() {
  const [isOpen, setIsOpen] = useState(false)
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const scrollAreaRef = useRef<HTMLDivElement>(null)

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    if (scrollAreaRef.current) {
      const scrollArea = scrollAreaRef.current;
      scrollArea.scrollTop = scrollArea.scrollHeight;
    }
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (input.trim() && !isLoading) {
      setIsLoading(true)
      
      const userMessage: Message = {
        id: Date.now(),
        content: input.trim(),
        role: 'user'
      }
      setMessages(prev => [...prev, userMessage])
      setInput('')

      try {
        const response = await fetch('https://dotslash-backend.onrender.com/marketing-bot', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            msg: input.trim()
          })
        });

        const data = await response.json();

        if (!response.ok) {
          throw new Error(data.error || 'API request failed');
        }

        const botMessage: Message = {
          id: Date.now(),
          content: data.response,
          role: 'bot'
        }
        setMessages(prev => [...prev, botMessage])
      } catch (error) {
        console.error('Chat Error:', error);
        const errorMessage: Message = {
          id: Date.now(),
          content: error instanceof Error ? 
            `Error: ${error.message}` : 
            'Sorry, I encountered an error processing your request.',
          role: 'bot'
        }
        setMessages(prev => [...prev, errorMessage])
      }
      
      setIsLoading(false)
    }
  }

  return (
    <>
      <Button
        variant="default"
        size="lg"
        className="fixed bottom-6 right-6 w-16 h-16 bg-gradient-to-r from-orange-600 to-orange-700 text-white rounded-full shadow-lg flex items-center justify-center hover:from-orange-700 hover:to-orange-800 transition-all duration-200 z-50"
        onClick={() => setIsOpen(prev => !prev)}
        aria-label={isOpen ? "Close chat" : "Open chat"}
      >
        <MessageCircle className="!w-7 !h-7" />
      </Button>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 20 }}
            transition={{ duration: 0.2 }}
            className="fixed bottom-24 right-6 w-96 h-[600px] bg-white rounded-lg shadow-xl overflow-hidden flex flex-col z-50"
          >
            <div className="flex justify-between items-center p-4 border-b bg-white">
              <div className="flex items-center gap-2">
                <Bot className="w-5 h-5 text-orange-500" />
                <h2 className="text-lg font-semibold text-orange-600">Chat Assistant</h2>
              </div>
              <Button variant="ghost" size="icon" onClick={() => setIsOpen(false)}>
                <X className="w-4 h-4 text-orange-600" />
              </Button>
            </div>

            <ScrollArea className="flex-grow p-4">
              <div ref={scrollAreaRef}>
                {messages.map((message) => (
                  <ChatMessage key={message.id} message={message} />
                ))}
                {isLoading && <TypingIndicator />}
              </div>
            </ScrollArea>

            <form onSubmit={handleSubmit} className="p-4 border-t bg-white">
              <div className="flex space-x-2">
                <Input
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  placeholder="Type your message..."
                  disabled={isLoading}
                  className="flex-grow"
                />
                <Button 
                  type="submit" 
                  variant="default" 
                  size="icon"
                  disabled={isLoading}
                  className="bg-orange-500 hover:bg-orange-600"
                >
                  <Send className="w-4 h-4" />
                </Button>
              </div>
            </form>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  )
}



================================================
FILE: frontend/src/components/CompanyInput.tsx
================================================
'use client';
import { useState } from "react";
import { Building2, MapPin, Loader2 } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Alert, AlertDescription } from "@/components/ui/alert";
import { MultiStepLoader } from "./MultiStepLoader";
import CompanyInfoDisplay from "./Analysis";

interface CompanyData {
  company: {
    official_name: string;
    industry_type: string;
    headquarters: string;
    key_products_services: string[];
    website: string;
  };
  competitors: {
    name: string;
    industry_type: string;
    headquarters: string;
    key_products_services: string[];
  }[];
}

const encodeURL = (str: string): string => {
  return encodeURI(str).replace(/'/g, '%27').replace(/,/g, '%2C');
};

const CompanyForm = () => {
  const [formData, setFormData] = useState({
    companyName: "",
    companyAddress: ""
  });
  const [errors, setErrors] = useState<{ companyName?: string; companyAddress?: string }>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitSuccess, setSubmitSuccess] = useState(false);
  const [companyData, setCompanyData] = useState<CompanyData | null>(null);

  const loadingStates = [
    { text: "Validating company information..." },
    { text: "Processing company details..." },
    { text: "Finalizing registration..." }
  ];

  const validateForm = (): boolean => {
    const newErrors: { companyName?: string; companyAddress?: string } = {};
    if (!formData.companyName.trim()) {
      newErrors.companyName = "Company name is required";
    }
    if (!formData.companyAddress.trim()) {
      newErrors.companyAddress = "Company address is required";
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitSuccess(false);

    if (!validateForm()) return;

    setIsSubmitting(true);
    try {
      const encodedCompanyName = encodeURL(formData.companyName);
      const encodedCompanyAddress = encodeURL(formData.companyAddress);

      const response = await fetch(
        `https://dotslash-backend.onrender.com/company?company=${encodedCompanyName}&location=${encodedCompanyAddress}`
      );

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data: CompanyData = await response.json();
      setCompanyData(data);
      setSubmitSuccess(true);
    } catch (error) {
      console.error("Error submitting form:", error);
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }));
    if (errors[name as keyof typeof errors]) {
      setErrors((prev) => ({
        ...prev,
        [name]: ""
      }));
    }
  };

  return (
    <>
      {submitSuccess && companyData ? (
        <div className="min-h-screen flex flex-col">
          <nav className="bg-white shadow-md p-4">
            <div className="container mx-auto">
              <h1 className="text-xl font-bold text-gray-800">Company Dashboard</h1>
            </div>
          </nav>
          <div className="flex-1 flex items-center justify-center p-4">
            <CompanyInfoDisplay companyData={companyData} />
          </div>
        </div>
      ) : (
        <div className="w-full max-w-4xl mx-auto p-4 pt-28">
          <Card className="overflow-hidden bg-white shadow-lg hover:shadow-xl transition-shadow duration-300">
            <CardHeader className="bg-gradient-to-r from-orange-50 to-orange-100 p-6">
              <CardTitle className="text-2xl font-bold text-gray-800">Company Details</CardTitle>
            </CardHeader>
            <CardContent className="p-6">
              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div className="space-y-2">
                    <Label htmlFor="companyName" className="flex items-center space-x-2 text-lg font-semibold text-gray-700">
                      <div className="bg-orange-500 p-2 rounded-full">
                        <Building2 className="h-4 w-4 text-white" />
                      </div>
                      <span>Company Name</span>
                    </Label>
                    <Input
                      id="companyName"
                      name="companyName"
                      type="text"
                      placeholder="Enter company name"
                      value={formData.companyName}
                      onChange={handleChange}
                      className={`w-full p-3 border rounded-md focus:ring-2 focus:ring-orange-500 focus:border-transparent transition-all duration-300 ${
                        errors.companyName ? "border-red-500" : "border-gray-300"
                      }`}
                    />
                    {errors.companyName && <p className="text-red-500 text-sm mt-1">{errors.companyName}</p>}
                  </div>

                  <div className="space-y-2">
                    <Label htmlFor="companyAddress" className="flex items-center space-x-2 text-lg font-semibold text-gray-700">
                      <div className="bg-black p-2 rounded-full">
                        <MapPin className="h-4 w-4 text-white" />
                      </div>
                      <span>Company Address</span>
                    </Label>
                    <Input
                      id="companyAddress"
                      name="companyAddress"
                      type="text"
                      placeholder="Enter company address"
                      value={formData.companyAddress}
                      onChange={handleChange}
                      className={`w-full p-3 border rounded-md focus:ring-2 focus:ring-black focus:border-transparent transition-all duration-300 ${
                        errors.companyAddress ? "border-red-500" : "border-gray-300"
                      }`}
                    />
                    {errors.companyAddress && <p className="text-red-500 text-sm mt-1">{errors.companyAddress}</p>}
                  </div>
                </div>

                {submitSuccess && (
                  <Alert className="mt-4 bg-green-50 text-green-800 border-green-200">
                    <AlertDescription>Company details successfully submitted!</AlertDescription>
                  </Alert>
                )}

                <div className="flex justify-end mt-6">
                  <Button
                    type="submit"
                    disabled={isSubmitting}
                    className="bg-orange-500 hover:bg-orange-600 text-white px-6 py-2 rounded-md font-medium transition-colors duration-300"
                  >
                    {isSubmitting ? (
                      <>
                        <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                        Submitting...
                      </>
                    ) : (
                      "Submit"
                    )}
                  </Button>
                </div>
              </form>
            </CardContent>
          </Card>
        </div>
      )}
      <MultiStepLoader loadingStates={loadingStates} loading={isSubmitting} duration={2000} loop={true} />
    </>
  );
};

export default CompanyForm;


================================================
FILE: frontend/src/components/ContactUs.tsx
================================================
import React, { useState } from "react";
import { motion } from "framer-motion";
import {
  Phone,
  Mail,
  MapPin,
  Clock,
  Send,
  User,
  MessageCircle,
  Star,
  MessageSquare,
} from "lucide-react";
import send from "@/hooks/sendMail";

// Define the type for the form data
interface FormData {
  name: string;
  email: string;
  subject: string;
  message: string;
}

// Define the type for the contact info items
interface ContactInfo {
  icon: React.ComponentType<{ className?: string }>;
  title: string;
  details: string[];
  color: string;
  bgColor: string;
}

const Contact: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    name: "",
    email: "",
    subject: "",
    message: "",
  });

  const [isSubmitted, setIsSubmitted] = useState<boolean>(false);

  const fadeIn = {
    initial: { opacity: 0, y: 20 },
    whileInView: { opacity: 1, y: 0 },
    viewport: { once: true },
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    // Do something with the form values.
		// ✅ This will be type-safe and validated.
		e.preventDefault(); // Prevent default form submission behavior

    // Extract values correctly from formData
    const { name, email, message } = formData;

    // Call send function
    send({ name, email, message });
		// toast.success("Thanks for Submitting Response");
		setFormData({
      name: "",
      email: "",
      subject: "",
      message: "",
    });
    setIsSubmitted(true);
  };

  const contactInfo: ContactInfo[] = [
    {
      icon: Phone,
      title: "Phone",
      details: ["+1 (555) 123-4567", "+1 (555) 765-4321"],
      color: "text-blue-500",
      bgColor: "bg-blue-50",
    },
    {
      icon: Mail,
      title: "Email",
      details: ["info@luminaryai.com", "support@luminaryai.com"],
      color: "text-orange-500",
      bgColor: "bg-orange-50",
    },
    {
      icon: MapPin,
      title: "Location",
      details: ["SVNIT Guest House", "Surat, Gujarat, India"],
      color: "text-green-500",
      bgColor: "bg-green-50",
    },
    {
      icon: Clock,
      title: "Business Hours",
      details: [
        "Monday - Friday: 9:00 AM - 6:00 PM",
        "Saturday: 10:00 AM - 4:00 PM",
        "Sunday: Closed",
      ],
      color: "text-purple-500",
      bgColor: "bg-purple-50",
    },
  ];

  return (
    <div className="min-h-screen from-white to-gray-50 pt-8">
      {/* Hero Section */}
      <section className="pt-16 pb-4">
        <div className="container mx-auto px-4">
          <motion.div
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
            className="text-center max-w-3xl mx-auto"
          >
            <div className="inline-flex items-center gap-2 px-4 py-2 bg-level-2 rounded-full mb-6">
              <MessageSquare className="w-5 h-5 text-white" />
              <span className="text-white font-medium">Contact Us</span>
            </div>
            <h1 className="text-4xl md:text-5xl font-bold mb-6 text-gray-700">
              Get in <span className="text-level-3">Touch</span>
            </h1>
            <p className="text-gray-600 text-lg leading-relaxed">
              We&apos;d love to hear from you. Let us know how we can help make your
              AI experience even better with your business
            </p>
          </motion.div>
        </div>
      </section>

      <section className="py-16">
        <div className="container mx-auto px-4">
          <div className="grid lg:grid-cols-2 gap-12">
            {/* Contact Information */}
            <motion.div
              variants={fadeIn}
              initial="initial"
              whileInView="whileInView"
              className="space-y-6"
            >
              <div className="grid sm:grid-cols-2 gap-6">
                {contactInfo.map((info, index) => (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.1 }}
                    className={`${info.bgColor} rounded-lg p-6 hover:scale-105 transition-transform`}
                  >
                    <div className="flex items-center gap-3 mb-4">
                      <info.icon className={`w-6 h-6 ${info.color}`} />
                      <h3 className="text-xl font-semibold">{info.title}</h3>
                    </div>
                    <div className="space-y-2">
                      {info.details.map((detail, idx) => (
                        <p key={idx} className="text-gray-600">
                          {detail}
                        </p>
                      ))}
                    </div>
                  </motion.div>
                ))}
              </div>

              {/* Google Maps iframe */}
              <div className="bg-gray-100 rounded-lg overflow-hidden">
                
Copy
<iframe
  title="SVNIT Guest House Location"
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3721.073509015362!2d72.7828153154024!3d21.16513848593489!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be04e7b7a7d0f4d%3A0x7a7d0f4d7a7d0f4d!2sSVNIT%20Guest%20House!5e0!3m2!1sen!2sin!4v1633080000000!5m2!1sen!2sin&markers=color:red%7Clabel:S%7C21.165138,72.785015"
  width="100%"
  height="400"
  style={{ border: 0 }}
  allowFullScreen
  loading="lazy"
></iframe>
              </div>
            </motion.div>

            {/* Contact Form */}
            <motion.div
              variants={fadeIn}
              initial="initial"
              whileInView="whileInView"
              className="bg-white rounded-xl p-8 border border-gray-100"
            >
              <div className="flex items-center gap-2 mb-6">
                <MessageCircle className="w-6 h-6 text-orange-500" />
                <h2 className="text-2xl font-bold">Send Us a Message</h2>
              </div>

              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="space-y-2">
                  <label htmlFor="name" className="text-gray-700 font-medium">
                    Full Name
                  </label>
                  <div className="relative">
                    <input
                      type="text"
                      id="name"
                      name="name"
                      value={formData.name}
                      onChange={handleChange}
                      className="w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-200 
                               focus:outline-none focus:ring-2 focus:ring-orange-500 
                               focus:border-transparent transition-all"
                      required
                    />
                    <User className="w-5 h-5 text-gray-400 absolute right-3 top-1/2 -translate-y-1/2" />
                  </div>
                </div>

                <div className="space-y-2">
                  <label htmlFor="email" className="text-gray-700 font-medium">
                    Email Address
                  </label>
                  <div className="relative">
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={formData.email}
                      onChange={handleChange}
                      className="w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-200 
                               focus:outline-none focus:ring-2 focus:ring-orange-500 
                               focus:border-transparent transition-all"
                      required
                    />
                    <Mail className="w-5 h-5 text-gray-400 absolute right-3 top-1/2 -translate-y-1/2" />
                  </div>
                </div>

                <div className="space-y-2">
                  <label htmlFor="subject" className="text-gray-700 font-medium">
                    Subject
                  </label>
                  <input
                    type="text"
                    id="subject"
                    name="subject"
                    value={formData.subject}
                    onChange={handleChange}
                    className="w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-200 
                             focus:outline-none focus:ring-2 focus:ring-orange-500 
                             focus:border-transparent transition-all"
                    required
                  />
                </div>

                <div className="space-y-2">
                  <label htmlFor="message" className="text-gray-700 font-medium">
                    Message
                  </label>
                  <textarea
                    id="message"
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    rows={4}
                    className="w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-200 
                             focus:outline-none focus:ring-2 focus:ring-orange-500 
                             focus:border-transparent transition-all resize-none"
                    required
                  />
                </div>

                <motion.button
                  type="submit"
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                  className={`w-full py-4 rounded-lg flex items-center justify-center gap-2
                           ${isSubmitted ? "bg-green-500" : "bg-orange-500"} 
                           text-white font-medium transition-colors`}
                >
                  {isSubmitted ? (
                    <>
                      <Star className="w-5 h-5" />
                      <span>Message Sent!</span>
                    </>
                  ) : (
                    <>
                      <Send className="w-5 h-5" />
                      <span>Send Message</span>
                    </>
                  )}
                </motion.button>
              </form>
            </motion.div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Contact;


================================================
FILE: frontend/src/components/DottedText.tsx
================================================
'use client'
import { useEffect, useRef } from 'react';

interface Point {
  x: number;
  y: number;
}

const DotMatrixText = () => {
  const text = 'Luminary AI';
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const dotsRef = useRef<Point[]>([]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d', { willReadFrequently: true });
    if (!ctx) return;

    // Set canvas size
    const updateCanvasSize = () => {
      canvas.width = window.innerWidth;
      canvas.height = 130;
    };
    updateCanvasSize();
    window.addEventListener('resize', updateCanvasSize);

    // Create dot matrix points
    const createDotMatrix = () => {
      ctx.fillStyle = 'white';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Draw text first to sample from
      ctx.fillStyle = 'black';
      ctx.font = 'bold 100px Arial';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(text, canvas.width / 2, canvas.height / 2);

      // Get image data
      const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
      const pixels = imageData.data;

      // Clear canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const points: Point[] = [];
      const dotSpacing = 8; // Space between dots

      // Scan for filled pixels in a grid pattern
      for (let y = 0; y < canvas.height; y += dotSpacing) {
        for (let x = 0; x < canvas.width; x += dotSpacing) {
          const index = (y * canvas.width + x) * 4;
          if (pixels[index] < 128) { // If pixel is dark (part of text)
            points.push({ x, y });
          }
        }
      }

      dotsRef.current = points;

      // Draw the dots
      ctx.fillStyle = 'gray-700';
      points.forEach(point => {
        ctx.beginPath();
        ctx.arc(point.x, point.y, 3, 0, Math.PI * 2); // Larger dots (radius 3)
        ctx.fill();
      });
    };

    createDotMatrix();

    return () => {
      window.removeEventListener('resize', updateCanvasSize);
    };
  }, []);

  return (
    <div className="relative px-0 py-0">
      <canvas
        ref={canvasRef}
        className=""
      />
    </div>
  );
};

export default DotMatrixText;


================================================
FILE: frontend/src/components/Footer.tsx
================================================
'use client'
import React from "react";
import { motion } from "framer-motion";
import {
  Bot,
  Mail,
  Twitter,
  Github,
  Instagram,
  MessageSquare,
  Command,
  Heart,
  LucideIcon,
  MapPin
} from "lucide-react";

interface FooterLinkProps {
  href: string;
  children: React.ReactNode;
}

interface SocialButtonProps {
  icon: LucideIcon;
  label: string;
  href: string;
}

const FooterLink: React.FC<FooterLinkProps> = ({ href, children }) => (
  <motion.a
    href={href}
    className="flex items-center gap-2 text-[#151616]/70 hover:text-[#151616] transition-colors"
    whileHover={{ x: 5 }}
    whileTap={{ scale: 0.95 }}>
    <Command className="w-4 h-4" />
    {children}
  </motion.a>
);

const SocialButton: React.FC<SocialButtonProps> = ({ icon: Icon, label, href }) => (
  <motion.a
    href={href}
    target="_blank"
    rel="noopener noreferrer"
    whileHover={{ rotate: 10 }}
    whileTap={{ scale: 0.9 }}
    className="group relative w-10 h-10 bg-white rounded-xl flex items-center justify-center 
      border-2 border-[#151616] shadow-[2px_2px_0px_0px_#151616] hover:shadow-[2px_2px_0px_0px_#151616] 
      hover:translate-y-[2px] hover:translate-x-[2px] hover:bg-level-1 transition-all">
    <Icon className="w-5 h-5 text-[#151616]" />
    <span
      className="absolute -top-8 scale-0 group-hover:scale-100 transition-transform 
      bg-[#151616] text-white text-xs py-1 px-2 rounded">
      {label}
    </span>
  </motion.a>
);

const Footer: React.FC = () => {
  return (
    <footer className="relative bg-white  pt-20 overflow-hidden">
      <div className="absolute top-0 left-0 right-0 h-0 bg-level-2" />

      <div className="container mx-auto px-6">
        

        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 py-16 border-t-2 border-[#151616]">
          <div className="md:col-span-2 space-y-6">
            <motion.div
              className="flex items-center gap-3"
              whileHover={{ scale: 1.02 }}>
              <div
                className="w-12 h-12 bg-level-2 rounded-xl flex items-center justify-center 
                border-2 border-[#151616] shadow-[4px_4px_0px_0px_#151616]">
                <Bot className="w-7 h-7 text-black" />
              </div>
              <h2 className="text-3xl font-bold text-level-4">Team 404 Not Found</h2>
            </motion.div>
            <div className="space-y-2 text-gray-600">
          <div className="flex items-center gap-2">
            <MapPin className="w-5 h-5" />
            <span>SVNIT, Surat, Gujarat</span>
          </div>
          <div className="flex items-center gap-2">
            <Mail className="w-5 h-5" />
            <a href="mailto:jd@gmail.com" className="hover:underline">mailme@gmail.com</a>
          </div>
        </div>
            <div className="flex gap-4">
              <SocialButton icon={Twitter} label="Twitter" href="#" />
              <SocialButton icon={Github} label="GitHub" href="#" />
              <SocialButton icon={Instagram} label="Instagram" href="#" />
              <SocialButton icon={MessageSquare} label="Discord" href="#" />
            </div>
          </div>

          <div className="space-y-4">
            <h3 className="font-bold text-lg">Navigation</h3>
            <div className="space-y-3">
              <FooterLink href="#">Features</FooterLink>
              <FooterLink href="#">Meditation</FooterLink>
              <FooterLink href="#">Sleep & Wellness</FooterLink>
              <FooterLink href="#">Recommendations</FooterLink>
            </div>
          </div>

          <div className="space-y-4">
            <h3 className="font-bold text-lg">Resources</h3>
            <div className="space-y-3">
              <FooterLink href="#">Help Center</FooterLink>
              <FooterLink href="#">Privacy Policy</FooterLink>
              <FooterLink href="#">Terms of Use</FooterLink>
              <FooterLink href="#">Contact Support</FooterLink>
            </div>
          </div>
        </div>

        <div
          className="border-t-2 border-[#151616]/10 py-6 flex flex-col md:flex-row 
          justify-between items-center gap-4">
          <div className="flex items-center gap-2 text-sm text-[#151616]/70">
            <span>© 2025 Luminary AI. All rights reserved.</span>
            <span className="flex items-center gap-1">
              Made with <Heart className="w-4 h-4 text-level-2" /> by Team
              404_#NotFound
            </span>
          </div>

          <motion.div
            className="flex items-center gap-3 bg-white px-4 py-2 rounded-full border-2 
              border-[#151616] shadow-[2px_2px_0px_0px_#151616]"
            whileHover={{ y: -2 }}>
            <span className="w-2 h-2 bg-level-2 rounded-full animate-pulse" />
            <span className="text-sm font-medium text-[#151616]">Support Available 24/7</span>
          </motion.div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;


================================================
FILE: frontend/src/components/Hero.tsx
================================================
// components/Hero.tsx
'use client';

import Link from 'next/link';
import DotMatrixText from './DottedText';

export default function Hero() {
  return (
    <div className="bg-white min-h-screen flex pt-[130px]  justify-center">
      <div className="text-center ">
        {/* Heading */}
        <h1 className="text-6xl font-bold text-gray-900 mb-2 ">
          Unlock The Power of
        </h1>
        <div className=''>
          <DotMatrixText />
        </div>

        {/* Subheading */}
        <p className="text-xl text-gray-600 mb-8">
          Harness AI agents for powerful solutions.
        </p>

        {/* Buttons */}
        <div className="flex justify-center space-x-4">
          <Link
            href="/build"
            className="px-6 py-3 bg-level-2 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            BUILD YOUR AGENT
          </Link>
          <Link
            href="/demo"
            className="px-6 py-3 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors"
          >
            TRY DEMO
          </Link>
        </div>
      </div>
    </div>
  );
}


================================================
FILE: frontend/src/components/MultiStepLoader.tsx
================================================
// MultiStepLoader.tsx
'use client'
import { cn } from "@/lib/utils";
import { AnimatePresence, motion } from "framer-motion";
import { useState, useEffect } from "react";

interface LoadingState {
  text: string;
}

interface CheckIconProps {
  className?: string;
  level?: 1 | 2 | 3;
}

interface LoaderCoreProps {
  loadingStates: LoadingState[];
  value?: number;
}

interface MultiStepLoaderProps {
  loadingStates: LoadingState[];
  loading: boolean;
  duration?: number;
  loop?: boolean;
}

const CheckIcon = ({ className, level = 1 }: CheckIconProps) => {
  const getColorClass = () => {
    switch (level) {
      case 1: return "text-white";
      case 2: return "text-orange-500";
      case 3: return "text-black";
      default: return "text-white";
    }
  };

  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      strokeWidth={1.5}
      stroke="currentColor"
      className={cn("w-6 h-6", getColorClass(), className)}
    >
      <path d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
    </svg>
  );
};

const CheckFilled = ({ className, level = 1 }: CheckIconProps) => {
  const getColorClass = () => {
    switch (level) {
      case 1: return "text-white";
      case 2: return "text-orange-500";
      case 3: return "text-black";
      default: return "text-white";
    }
  };

  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="currentColor"
      className={cn("w-6 h-6", getColorClass(), className)}
    >
      <path
        fillRule="evenodd"
        d="M2.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75S2.25 17.385 2.25 12Zm13.36-1.814a.75.75 0 1 0-1.22-.872l-3.236 4.53L9.53 12.22a.75.75 0 0 0-1.06 1.06l2.25 2.25a.75.75 0 0 0 1.14-.094l3.75-5.25Z"
        clipRule="evenodd"
      />
    </svg>
  );
};

const LoaderCore = ({ loadingStates, value = 0 }: LoaderCoreProps) => {
  const getLevel = (index: number): 1 | 2 | 3 => {
    const totalStates = loadingStates.length;
    if (index < totalStates / 3) return 1;
    if (index < (totalStates / 3) * 2) return 2;
    return 3;
  };

  return (
    <div className="flex relative justify-start max-w-xl mx-auto flex-col mt-40">
      {loadingStates.map((loadingState, index) => {
        const distance = Math.abs(index - value);
        const opacity = Math.max(1 - distance * 0.2, 0);
        const level = getLevel(index);
        
        return (
          <motion.div
            key={index}
            className={cn("text-left flex gap-2 mb-4")}
            initial={{ opacity: 0, y: -(value * 40) }}
            animate={{ opacity: opacity, y: -(value * 40) }}
            transition={{ duration: 0.5 }}
          >
            <div className="flex items-center">
              {index > value && (
                <CheckIcon level={level} />
              )}
              {index <= value && (
                <CheckFilled level={level} />
              )}
            </div>
            <span
              className={cn(
                level === 1 && "text-white",
                level === 2 && "text-orange-500",
                level === 3 && "text-black",
                value === index && "opacity-100",
                value !== index && "opacity-70"
              )}
            >
              {loadingState.text}
            </span>
          </motion.div>
        );
      })}
    </div>
  );
};

export const MultiStepLoader = ({
  loadingStates = [
    // Level 1 - Initial validation (White)
    { text: "Initializing submission process..." },
    { text: "Validating form data..." },
    // Level 2 - Processing (Orange)
    { text: "Processing company information..." },
    { text: "Updating business registry..." },
    { text: "Generating confirmation details..." },
    // Level 3 - Finalizing (Black)
    { text: "Running final checks..." },
    { text: "Saving to secure database..." },
    { text: "Completing registration..." }
  ],
  loading,
  duration = 2000,
  loop = true
}: MultiStepLoaderProps) => {
  const [currentState, setCurrentState] = useState(0);

  useEffect(() => {
    if (!loading) {
      setCurrentState(0);
      return;
    }

    const timeout = setTimeout(() => {
      setCurrentState((prevState) =>
        loop
          ? prevState === loadingStates.length - 1
            ? 0
            : prevState + 1
          : Math.min(prevState + 1, loadingStates.length - 1)
      );
    }, duration);

    return () => clearTimeout(timeout);
  }, [currentState, loading, loop, loadingStates.length, duration]);

  return (
    <AnimatePresence mode="wait">
      {loading && (
        <motion.div
          initial={{
            opacity: 0,
          }}
          animate={{
            opacity: 1,
          }}
          exit={{
            opacity: 0,
          }}
          className="w-full h-full fixed inset-0 z-[100] flex items-center justify-center backdrop-blur-sm bg-black/30"
        >
          <div className="h-96 relative">
            <LoaderCore value={currentState} loadingStates={loadingStates} />
          </div>
          <div className="bg-gradient-to-t inset-x-0 z-20 bottom-0 bg-black/80 h-full absolute [mask-image:radial-gradient(900px_at_center,transparent_30%,white)]" />
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default MultiStepLoader;


================================================
FILE: frontend/src/components/Navbar.tsx
================================================
// components/Navbar.tsx
'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { motion } from 'framer-motion';
import { Menu, X, Home, Star, MessageCircle, User, Settings, Contact } from 'lucide-react';
import Image from 'next/image';

interface NavLinkProps {
  href: string;
  label: string;
  icon: React.ElementType;
}

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const pathname = usePathname();

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const NavLink = ({ href, label, icon: Icon }: NavLinkProps) => {
    const isActive = pathname === href;

    return (
      <Link href={href}>
        <motion.div
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          className={`flex items-center gap-2 px-4 py-2 rounded-xl transition-all duration-300 ${isActive
            ? 'bg-black text-white shadow-lg' // Level 3 (Black) for active state
            : 'text-black hover:bg-orange-500 hover:text-white' // Level 2 (Orange) for hover
            }`}
        >
          <Icon className="w-5 h-5" />
          <span className="font-medium">{label}</span>
        </motion.div>
      </Link>
    );
  };

  const links = [
    { href: '/', label: 'Home', icon: Home },
    { href: '/explore', label: 'Explore', icon: Star },
    { href: '/build', label: 'Build with Us', icon: MessageCircle },
    { href: '/sectors', label: 'Sectors', icon: Settings },
    { href: '/contact', label: 'Contact Us', icon: Contact },
  ];

  return (
    <nav
      className={`fixed top-0 w-full z-50 transition-all duration-300 ${scrolled ? 'bg-white/80 backdrop-blur-md shadow-lg' : 'bg-white' // Level 1 (White) for background
        }`}
    >
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo Section */}
          <motion.div
            className="flex items-center gap-3"
            whileHover={{ scale: 1.05 }}
          >
            <div className="h-10 w-10 rounded-xl flex items-center justify-center"> {/* Level 3 (Black) for logo background */}
              <Image src="/logo.svg" width={50} height={50} alt="AI Competitor" className="h-8 w-8" />
            </div>
            <span className="text-xl font-bold text-black">Luminary AI</span> {/* Level 3 (Black) for text */}
          </motion.div>

          {/* Desktop Links */}
          <div className="hidden md:flex items-center gap-4">
            {links.map((link) => (
              <NavLink key={link.href} {...link} />
            ))}
          </div>

          {/* Sign In Button (Desktop) */}
          <div className="hidden md:flex items-center gap-4">
            <Link href="/signin">
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="flex items-center gap-2 px-6 py-2 rounded-xl bg-black text-white font-medium hover:bg-orange-500 transition-colors shadow-lg" // Level 3 (Black) for button
              >
                <User className="w-5 h-5" />
                Sign In
              </motion.button>
            </Link>
          </div>

          {/* Mobile Menu Toggle */}
          <motion.button
            whileTap={{ scale: 0.95 }}
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden"
          >
            {isOpen ? (
              <X className="w-6 h-6 text-black" />
            ) : (
              <Menu className="w-6 h-6 text-black" />
            )}
          </motion.button>
        </div>

        {/* Mobile Menu */}
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="md:hidden py-4 border-t border-orange-500" // Level 2 (Orange) for border
          >
            <div className="space-y-2">
              {links.map((link) => (
                <NavLink key={link.href} {...link} />
              ))}
              <Link href="/signin">
                <motion.button
                  whileTap={{ scale: 0.95 }}
                  className="w-full flex items-center justify-center gap-2 px-4 py-2 rounded-xl bg-black text-white font-medium shadow-lg hover:bg-orange-500 transition-colors" // Level 3 (Black) for button
                >
                  <User className="w-5 h-5" />
                  Sign In
                </motion.button>
              </Link>
            </div>
          </motion.div>
        )}
      </div>
    </nav>
  );
}


================================================
FILE: frontend/src/components/ScrollButton.tsx
================================================
import React, { useState, useEffect } from "react";
import { ArrowUp } from "lucide-react";

const ScrollButton = () => {
  const [visible, setVisible] = useState(false);

  // Use useEffect to properly handle event listener
  useEffect(() => {
    const toggleVisibility = () => {
      if (window.pageYOffset > 300) {
        setVisible(true);
      } else {
        setVisible(false);
      }
    };

    window.addEventListener("scroll", toggleVisibility);

    // Cleanup event listener on component unmount
    return () => {
      window.removeEventListener("scroll", toggleVisibility);
    };
  }, []);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  return (
    <button
      onClick={scrollToTop}
      className={`fixed bottom-8 right-8 p-3 rounded-full bg-orange-500 hover:bg-orange-600 text-white shadow-lg transition-all duration-300 ease-in-out transform hover:scale-110 focus:outline-none focus:ring-2 focus:ring-orange-400 focus:ring-opacity-50 ${
        visible
          ? "opacity-100 translate-y-0"
          : "opacity-0 translate-y-8 pointer-events-none"
      }`}
      aria-label="Scroll to top">
      <ArrowUp className="w-6 h-6" />
    </button>
  );
};

export default ScrollButton;



================================================
FILE: frontend/src/components/Signin.tsx
================================================
"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { auth, googleProvider } from "@/lib/firebase";
import { signInWithEmailAndPassword, signInWithPopup } from "firebase/auth";
import { motion } from "framer-motion";
import { Mail, Lock, Eye, EyeOff, AlertCircle, ChevronRight, LogIn, Car } from "lucide-react";
import Image from "next/image";

const SignIn: React.FC = () => {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  useEffect(() => {
    const canvas = document.getElementById("gradient-canvas") as HTMLCanvasElement;
    if (canvas) {
      const ctx = canvas.getContext("2d");
      if (ctx) {
        const animate = () => {
          canvas.width = window.innerWidth;
          canvas.height = window.innerHeight;

          const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
          gradient.addColorStop(0, "#FFFFFF");
          gradient.addColorStop(1, "#FFA500");
          ctx.fillStyle = gradient;
          ctx.fillRect(0, 0, canvas.width, canvas.height);

          requestAnimationFrame(animate);
        };
        animate();
      }
    }
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleEmailSignIn = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      await signInWithEmailAndPassword(auth, formData.email, formData.password);
      router.push("/dashboard");
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleSignIn = async () => {
    try {
      const result = await signInWithPopup(auth, googleProvider);
      if (result.user) {
        router.push("/dashboard");
      }
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      }
    }
  };

  return (
    <div className="min-h-screen w-full bg-gradient-to-b from-white to-gray-50 flex">
      {/* Left Section: Content */}
      <motion.div
        initial={{ opacity: 0, x: -20 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.6 }}
        className="hidden lg:flex w-1/2 relative overflow-hidden"
      >
        {/* Background with gradient and pattern */}
        <div className="absolute inset-0 bg-gradient-to-br from-orange-500 via-orange-600 to-orange-700">
          {/* Modern grid pattern */}
          <div
            className="absolute inset-0"
            style={{
              backgroundImage: `radial-gradient(circle at 1px 1px, rgba(255,255,255,0.1) 1px, transparent 0)`,
              backgroundSize: "32px 32px",
            }}
          ></div>

          {/* Floating shapes */}
          <div className="absolute top-20 right-20 w-64 h-64 bg-orange-400/20 rounded-full blur-3xl"></div>
          <div className="absolute bottom-40 left-20 w-72 h-72 bg-white/10 rounded-full blur-3xl"></div>
        </div>

        {/* Content Container */}
        <div className="relative w-full p-12 flex flex-col justify-between z-10">
          {/* Top Section */}
          <div>
            <Link
              href="/"
              className="flex items-center gap-2 text-white mb-16 group"
            >
              <div className="bg-white/10 p-2 rounded-lg backdrop-blur-sm group-hover:bg-white/20 transition-all">
                <Image src={"logo.svg"} height={50} width={50} alt="logo" className="w-8 h-8" />
              </div>
              <span className="text-2xl font-bold">Luminary AI</span>
            </Link>

            <div className="space-y-8">
              <div>
                <h1 className="text-5xl font-bold text-white mb-6 leading-tight">
                  Your Journey
                  <br />
                  Begins Here
                </h1>
              </div>

            </div>
          </div>

          {/* Bottom Stats Section */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6 }}
            className="bg-white/10 backdrop-blur-sm rounded-2xl p-6"
          >
            <div className="grid grid-cols-3 gap-8">
              {[
                { value: "50K+", label: "Happy Customers" },
                { value: "100+", label: "Users" },
                { value: "4.9/5", label: "User Rating" },
              ].map((stat, index) => (
                <div key={index} className="text-center">
                  <h4 className="text-2xl font-bold text-white mb-1">
                    {stat.value}
                  </h4>
                  <p className="text-orange-50/80 text-sm">{stat.label}</p>
                </div>
              ))}
            </div>
          </motion.div>
        </div>
      </motion.div>

      {/* Right Section: Login Form */}
      <motion.div
        initial={{ opacity: 0, x: 20 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.6 }}
        className="w-full lg:w-1/2 flex items-center justify-center p-6 md:p-12"
      >
        <div className="w-full max-w-md">
          {/* Mobile Logo */}
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className="lg:hidden flex flex-col items-center gap-4 mb-8"
          >
            <Link href="/" className="flex items-center gap-2 group">
              <div className="bg-orange-50 p-2 rounded-lg group-hover:bg-orange-100 transition-all">
                <Car className="w-8 h-8 text-orange-500" />
              </div>
              <span className="text-2xl font-bold">
                <span className="text-gray-900">Car</span>
                <span className="text-orange-500">Rental</span>
              </span>
            </Link>
          </motion.div>

          <div className="text-center mb-8">
            <h2 className="text-3xl font-bold mb-2">Login to Your Account</h2>
            <p className="text-gray-600">Welcome back! Please enter your details</p>
          </div>

          <form onSubmit={handleEmailSignIn} className="space-y-6">
            <div className="space-y-2">
              <label className="text-sm font-medium text-gray-700">Email</label>
              <div className="relative">
                <input
                  type="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 pl-12 border rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent transition-all"
                  placeholder="Enter your email"
                />
                <Mail className="w-5 h-5 text-gray-400 absolute left-4 top-3.5" />
              </div>
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium text-gray-700">Password</label>
              <div className="relative">
                <input
                  type={showPassword ? "text" : "password"}
                  name="password"
                  value={formData.password}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 pl-12 pr-12 border rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent transition-all"
                  placeholder="Enter your password"
                />
                <Lock className="w-5 h-5 text-gray-400 absolute left-4 top-3.5" />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-4 top-3.5 text-gray-400 hover:text-gray-600 transition-colors"
                >
                  {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                </button>
              </div>
            </div>

            {error && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                className="flex items-center gap-2 text-red-500 bg-red-50 p-3 rounded-lg"
              >
                <AlertCircle className="w-5 h-5" />
                <p className="text-sm">{error}</p>
              </motion.div>
            )}

            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              type="submit"
              disabled={loading}
              className="w-full px-4 py-3 bg-orange-500 text-white rounded-lg font-medium hover:bg-orange-600 transition-colors flex items-center justify-center gap-2"
            >
              <LogIn className="w-5 h-5" />
              {loading ? "Signing In..." : "Sign In"}
            </motion.button>

            <div className="relative my-8">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-gray-200"></div>
              </div>
              <div className="relative flex justify-center">
                <span className="px-4 text-sm text-gray-500 bg-gradient-to-b from-white to-gray-50">or</span>
              </div>
            </div>

            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              type="button"
              onClick={handleGoogleSignIn}
              className="w-full px-4 py-3 bg-white border border-gray-200 text-gray-700 rounded-lg font-medium hover:bg-gray-50 transition-colors flex items-center justify-center gap-2"
            >
              <Image
                src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAABR1BMVEX////lQzU0o1NCgO/2twQ9fu9rl/FynvPt8v0xee72tADlQTMwolDkPS7kOyv2uADkNCL98O8ln0kpoEwanUPkNibkMR3nVEjp9ez3zMntioPrenL+9vX++vr74uD73Zj3+v7f7+P519T2xMHwmZP40c7ukYroYFXnUUXzsq3xpaDkOzb98dj/+/HA0vn74auRsvX868VVjPDM2/rK5dGDw5NjtXmn1LJXsG/B4MlMrGZCfffi8eX1u7fsgXrpaF/jKA7re3PyqZXqb2XujDvyoiv1syHpYz3sf0D3wDTwlzPnVT350XTrc0H63Z7nWTD4y1z++ej3w0mnwvf4zm2auPbe5/yFtFzJvUyeul5psF3WvUGVyqKuulXjvTSz0J2ixd1TnrRKo4xMjdtPl79Jn5lGpnFJiORhs3ZKkslJm6Y+pGd8quAEW6SpAAAHw0lEQVR4nO2b2X/bRBCAZUVJG12WddnO4cZOYjtp0yP1FZPELYVCIUAPChTcQjlKKPz/z8i3LUurlbUrrf2b76V9SKX9MrMzu2OX4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAk0yhlM/v7+fzh4XMbtKLIcpO4eL4siLZDlof5y+PlOz2wUUpk/TaopPZL3ckW7MUSUrNIEmKatlKZ+uikPQaI1A6qEiaqrjcZjwVVVOz5VLSK12IUtlZvDtynpaS84NLJ5k5ztoqht3YUrWzx0u0KUuXihVCbyhpKZdLsiUPO1aY8E0H0tpegmQtdWxUaQlwVB5tMx7HwratLKo3QNG2GN6PuweqGs2vF0dLOkpaxI98NXx98XTUKkym6s6WTcSvh2IzGMbDrEXKL9UL4zZru/FYi1hh3KgpphrHzhONWIaOkB4xlKmFavQS6oFdTlpsxKFCOENHaNtsXJT3yWfoCPtx0nI9jsg1CTdqZSdpO46uYGfVBVc+glkWysz+qkewRK+KqhUWTm2ZFDVBpcpCBHcroRu9NCTo59QsC4LcVqjLhKJamnP/r2az2api25aK+PWwkaLchY1tJ6ma3SkfHWYyO30ymcOjcsXWfAZWSpYJwQxuGXX0UuW8R+XfyW9JmsfUio09yHGYm1DSUluIi17+8dxklZE96Nx48fyqRwHrLbimV4ykKFfAmTlJlnSBcS7JlKcmkEqVDUGug5GjinqA+bRCZ3R0YGUP4tRRSeuEGAkeDS7RrKQotxt8mJHs41CPLFRUhlKUOw7s9YoUelL2RFNSrAhmAo9dCx1KyswIcp8GhdB6stBzmRE8SX92GxlEi5ER2cLcEtOfVxGK1nbSK4yKIAjpp1/c9t2DnaQXGJV7Yk9R+NInUxUmxiuReCb0SX/lqSipTH70F4Y7ojBUfPr1fKZK2n7SC4zM1cjQydRv5hStraTXF5kTYUJ6rm1IqaXfhNwDUZh2dLUN+zDp9UXnasbQ1TZUJj4qikhamCWdnrSNFaij7iR1tQ2Vmc9sI3Br3nDcNlYihKN271IctA31MunVEeDEI4TjtmGvQgg9tuG4bSjZpFdHgm/9DJ3N+N1F0qsjwXNfQ2czniS9OhJ4Fpohz/EecXMjIjdoCr5w9/spxFuYhpvr0Vjbo2h4xz9JBfEOruFaNNZvUjT0LaU9MLdhZMPNHygaep1oRrzEfEZ0w7sUDa/8DcWr2AxfUTT8HmF4Ly7D9fsUDRHtUHwQmyHNdvHSfxvillLGDRENX3wRm+EGPcETlCHumS264ekeGC5u6C8oiLgPYduQiRiugWEUmKilVA3Z6Ic0DZ8jDOM709A0ZONcSrHjs3G3oGrIxP2Q6rmUiTs+1dsTE3OazdcUDcnM2qIa0rzjE5mXRjZ8SNMQdclP421EvHkpypDmrA1RTEXhxzM8w40bGKCCSHNe6l9MxXdt45rce276+62fknuNBz6fHwriT7zMmzli73nov1mptkPOp9SIwhvewagTe81rf0OqzYLz3ojis5/5PjKxIG74lxq6pdRzI4q/8EP0LqG3oDrKJtVCw81/n0YQ3/JjSAXxFapnknmFP64LlNMkJoLEdiLCj+qptM9smjpNgp/GLJJ4x11UktL85KnPyXSaOk1iFpkn8Y5TxJFmc4/EG5BMp+kb3g2JYoMKIdXr75Bxmo6bxKxiLeoL9pAhpHqxGPLM3SRm8zRyPb2PKqTUe0WP4beG3noKOoqtaI9HHNjiSVKu//8tZpuEK08bUR6+h/CLKUl7JzfxnVM1/RWjdEXEeW2N8jdNJpwI7iZBTvEGcgJA+14x5lcdbbi4IrLK0L7eT5ELEFx4L6IjSPvyO003KIi8wYc/v+1tBAyp6J/YJqAKzQBZb4Z85sM1ZJGJNYQcd2YGJipv1kP1/t8+CRCMNYQcd20EKxo8fhhrbfN9gGKsIeS4cwxDp+C08U6pxYYp8+bvqANp3CHkuGZgsekhm63gKWqtrvd/X/q/f3yCCGE8B7YpWoHFZujYbqL2Y67Z0kf5IMt/+ivG1gsnS8MoNoN163qr6d07io6ePvWbks2//ArqJvXpxTw49XQsafL1Zi03DmYuVzzrNmRTdyeC+eFvz6ZI9cN7X+pYW3Ekaeimybdb141Gq9XmdVM3PNPc4P/xylTaU1If2lgFdcZzCOpH9I/zbSOJHO2RCz7aLIL54dSVqTG3wimKYfIUH6PtahsxXQu9CFFtwiAb76cVE9qEA5p0FJ0DzqRtxDS6iFtxcsBJqspQVxwdcDbjmlwkoGh+XF9nQdApN3MnE0LozgGHBUHncoBs4REwjP+SdhtyHv50g4UZdhJCkQaFzSibeN/QiYkm8c24yLiOKrU22SOc3iD39RxS1E1yYZRZ2oITajypMOrt86RlfOgaJIqqITMZwAHnjcipKoccJcdO7TqSo2w2GCuhHtSu9UVz1dCvI3/TIRaKdXmB9uj8mzr78RuRa7bNcIE0AkbHDFLsyqb3xNAjeqbcXZ7wTVHstnifuehYTjZM3m8mvhTkzurXvKl7eMr9IXG70a0tWXJ60Bvh11u82UfXB38ajltzBeRmyBWLtdrZWa1WO18xMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAQ/wNhUPDo3tE+ZAAAAABJRU5ErkJggg=="
                alt="Google"
                className="w-6 h-6"
                width={50}
                height={50}
              />
              Sign in with Google
            </motion.button>
          </form>

          <p className="mt-8 text-center text-gray-600">
            Don&apos;t have an account?{" "}
            <Link
              href="/signup"
              className="text-orange-500 font-semibold hover:text-orange-600 transition-colors inline-flex items-center gap-1"
            >
              Sign up
              <ChevronRight className="w-4 h-4" />
            </Link>
          </p>
        </div>
      </motion.div>
    </div>
  );
};

export default SignIn;


================================================
FILE: frontend/src/components/Signup.tsx
================================================
'use client'
import React, { useState } from "react";
import { motion } from "framer-motion";
import { Mail, Lock, ChevronRight, Eye, EyeOff, AlertCircle } from "lucide-react";

const Register = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [showPassword, setShowPassword] = useState({
    password: false,
    confirmPassword: false,
  });
  const [error] = useState<string | null>(null);

  return (
    <div className="min-h-screen w-full bg-gradient-to-b from-white to-gray-50 flex justify-center">
      {/* Right Section: Register Form */}
      <motion.div
        initial={{ opacity: 0, x: 20 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.6 }}
        className="w-full lg:w-1/2 flex items-center justify-center p-6 md:p-12">
        <div className="w-full max-w-md">
          <div className="text-center mb-8">
            <h2 className="text-3xl font-bold mb-2">Create Your Account</h2>
            <p className="text-gray-600">Join us for the best experience</p>
          </div>

          <form className="space-y-6">
            <div className="space-y-2">
              <label className="text-sm font-medium text-gray-700">Email</label>
              <div className="relative">
                <input
                  type="email"
                  value={formData.email}
                  onChange={(e) =>
                    setFormData({ ...formData, email: e.target.value })
                  }
                  required
                  className="w-full px-4 py-3 pl-12 border rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent transition-all"
                  placeholder="Enter your email"
                />
                <Mail className="w-5 h-5 text-gray-400 absolute left-4 top-3.5" />
              </div>
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium text-gray-700">Password</label>
              <div className="relative">
                <input
                  type={showPassword.password ? "text" : "password"}
                  value={formData.password}
                  onChange={(e) =>
                    setFormData({ ...formData, password: e.target.value })
                  }
                  required
                  className="w-full px-4 py-3 pl-12 pr-12 border rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent transition-all"
                  placeholder="Create a password"
                />
                <Lock className="w-5 h-5 text-gray-400 absolute left-4 top-3.5" />
                <button
                  type="button"
                  onClick={() =>
                    setShowPassword({
                      ...showPassword,
                      password: !showPassword.password,
                    })
                  }
                  className="absolute right-4 top-3.5 text-gray-400 hover:text-gray-600 transition-colors">
                  {showPassword.password ? (
                    <EyeOff className="w-5 h-5" />
                  ) : (
                    <Eye className="w-5 h-5" />
                  )}
                </button>
              </div>
            </div>

            <div className="space-y-2">
              <label className="text-sm font-medium text-gray-700">Confirm Password</label>
              <div className="relative">
                <input
                  type={showPassword.confirmPassword ? "text" : "password"}
                  value={formData.confirmPassword}
                  onChange={(e) =>
                    setFormData({ ...formData, confirmPassword: e.target.value })
                  }
                  required
                  className="w-full px-4 py-3 pl-12 pr-12 border rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent transition-all"
                  placeholder="Confirm your password"
                />
                <Lock className="w-5 h-5 text-gray-400 absolute left-4 top-3.5" />
                <button
                  type="button"
                  onClick={() =>
                    setShowPassword({
                      ...showPassword,
                      confirmPassword: !showPassword.confirmPassword,
                    })
                  }
                  className="absolute right-4 top-3.5 text-gray-400 hover:text-gray-600 transition-colors">
                  {showPassword.confirmPassword ? (
                    <EyeOff className="w-5 h-5" />
                  ) : (
                    <Eye className="w-5 h-5" />
                  )}
                </button>
              </div>
            </div>

            {error && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                className="flex items-center gap-2 text-red-500 bg-red-50 p-3 rounded-lg">
                <AlertCircle className="w-5 h-5" />
                <p className="text-sm">{error}</p>
              </motion.div>
            )}

            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              type="submit"
              className="w-full px-4 py-3 bg-orange-500 text-white rounded-lg font-medium hover:bg-orange-600 transition-colors flex items-center justify-center gap-2">
              Create Account
            </motion.button>

            <div className="relative my-8">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-gray-200"></div>
              </div>
              <div className="relative flex justify-center">
                <span className="px-4 text-sm text-gray-500 bg-gradient-to-b from-white to-gray-50">
                  or continue with
                </span>
              </div>
            </div>

            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              type="button"
              className="w-full px-4 py-3 bg-white border border-gray-200 text-gray-700 rounded-lg font-medium hover:bg-gray-50 transition-colors flex items-center justify-center gap-2">
              <img
                src="https://cdn4.iconfinder.com/data/icons/logos-brands-7/512/google_logo-google_icongoogle-512.png"
                alt="Google"
                className="w-5 h-5"
              />
              Sign up with Google
            </motion.button>
          </form>

          <p className="mt-8 text-center text-gray-600">
            Already have an account?{" "}
            <motion.a
              whileHover={{ scale: 1.05 }}
              href="/login"
              className="text-orange-500 font-semibold hover:text-orange-600 transition-colors inline-flex items-center gap-1">
              Sign in
              <ChevronRight className="w-4 h-4" />
            </motion.a>
          </p>
        </div>
      </motion.div>
    </div>
  );
};

export default Register;



================================================
FILE: frontend/src/components/Sponsors.tsx
================================================
import Image from 'next/image';
import React from 'react';

const BrandLogos = () => {
  const brands = [
    {
      name: 'Weybee',
      imgUrl: '/logo1.png',
      color: '#FF6B6B'
    },
    {
      name: 'Brew and Beans',
      imgUrl: '/logo2.png',
      color: '#4D4D4D'
    },
    {
      name: 'Avadh Group',
      imgUrl: '/logo6.png',
      color: '#00A0DC'
    },
    {
      name: 'Craft Cart',
      imgUrl: '/logo3.png',
      color: '#4A90E2'
    },
    {
      name: 'Serene Stays',
      imgUrl: '/logo4.png',
      color: '#E50914'
    },
    {
      name: 'Green Valley Grocery',
      imgUrl: '/logo5.png',
      color: '#00A0DC'
    },

  ];

  return (
    <div className="w-screen mx-auto py-12 bg-white">
      <h2 className="text-4xl font-bold text-gray-900 text-center tracking-wider mb-8">
          Trusted by Businesses like
        </h2>
      
      <div className="flex flex-wrap justify-center items-center gap-12 px-4">
        {brands.map((brand) => (
          <div
            key={brand.name}
            className="group relative transition-all duration-300 ease-in-out cursor-pointer"
          >
            <div className="w-32 h-32 flex items-center justify-center transform transition-all duration-300 group-hover:-translate-y-2">
              <Image
                src={brand.imgUrl}
                width={500}
                height={500}
                alt={`${brand.name} logo`}
                className="w-full h-full object-contain transition-all duration-300 filter grayscale group-hover:grayscale-0"
                style={{
                  '--hover-color': brand.color
                } as React.CSSProperties}
              />
            </div>
            <div 
              className="absolute bottom-0 left-0 w-0 h-0.5 bg-gray-200 group-hover:w-full transition-all duration-300"
              style={{ 
                backgroundColor: 'var(--hover-color)',
                opacity: 0,
                transition: 'opacity 0.3s, width 0.3s',
              }}
            ></div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default BrandLogos;


================================================
FILE: frontend/src/components/StartBusiness.tsx
================================================
"use client";

import React from "react";
import { motion } from "framer-motion";
import {
  Star,
  Shield,
  Car,
  CheckCircle,
  Award,
  Settings,
  Users,
  CreditCard,
  Clock,
  BarChart,
  PhoneCall,
  Calendar,
} from "lucide-react";

const About: React.FC = () => {
  const fadeIn = {
    initial: { opacity: 0, y: 20 },
    whileInView: { opacity: 1, y: 0 },
    viewport: { once: true },
  };

  const featureCards = [
    {
      icon: Shield,
      title: "Secure Booking",
      description: "Advanced security measures for safe transactions",
      color: "text-blue-500",
      bgColor: "bg-blue-50",
    },
    {
      icon: Car,
      title: "Wide Selection",
      description: "Diverse fleet of vehicles for every need",
      color: "text-orange-500",
      bgColor: "bg-orange-50",
    },
    {
      icon: Users,
      title: "24/7 Support",
      description: "Round-the-clock customer assistance",
      color: "text-green-500",
      bgColor: "bg-green-50",
    },
    {
      icon: CreditCard,
      title: "Easy Payments",
      description: "Flexible and secure payment options",
      color: "text-purple-500",
      bgColor: "bg-purple-50",
    },
  ];

  const advancedFeatures = [
    {
      icon: Clock,
      title: "Real-time Availability",
      description: "Check car availability instantly with live updates",
      color: "text-indigo-500",
      bgColor: "bg-indigo-50",
    },
    {
      icon: Calendar,
      title: "Flexible Duration",
      description: "Rent cars from hours to months with flexible terms",
      color: "text-pink-500",
      bgColor: "bg-pink-50",
    },
    {
      icon: CreditCard,
      title: "Integrated Payments",
      description: "Secure payment gateway with multiple options",
      color: "text-yellow-500",
      bgColor: "bg-yellow-50",
    },
    {
      icon: BarChart,
      title: "Admin Analytics",
      description: "Comprehensive dashboards with valuable insights",
      color: "text-teal-500",
      bgColor: "bg-teal-50",
    },
    {
      icon: PhoneCall,
      title: "24/7 Support",
      description: "Round-the-clock comprehensive customer assistance",
      color: "text-red-500",
      bgColor: "bg-red-50",
    },
  ];

  const stats = [
    { value: "15K+", label: "Happy Customers" },
    { value: "150+", label: "Locations" },
    { value: "98%", label: "Satisfaction Rate" },
    { value: "24/7", label: "Customer Support" },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-white to-gray-50 pt-8">
      {/* Hero Section */}
      <section className="py-16">
        <div className="container mx-auto px-4">
          <motion.div
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
            viewport={{ once: true }}
            className="text-center max-w-3xl mx-auto"
          >
            <div className="inline-flex items-center gap-2 px-4 py-2 bg-orange-100 rounded-full mb-6">
              <Star className="w-5 h-5 text-orange-500" />
              <span className="text-orange-700 font-medium">Build Your Business with Us</span>
            </div>
            <h1 className="text-4xl md:text-5xl font-bold mb-6 text-level-3">
              KickStart Your  <span className="text-orange-500"> Car Rentals</span> with Us
             
            </h1>
            <p className="text-gray-600 text-lg leading-relaxed">
              Welcome to CarRental, where we redefine the car rental experience.
              Our mission is to provide seamless, reliable, and affordable car
              rentals for everyone, everywhere.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Mission Section */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4">
          <motion.div
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
            viewport={{ once: true }}
            className="grid md:grid-cols-2 gap-12 items-center"
          >
            <div>
              <div className="flex items-center gap-2 mb-4">
                <Award className="w-6 h-6 text-orange-500" />
                <h2 className="text-3xl font-bold">Our Mission</h2>
              </div>
              <p className="text-gray-600 leading-relaxed mb-6">
                Our mission is to revolutionize the car rental industry by
                providing a seamless, transparent, and customer-centric
                experience. We believe in making car rentals accessible,
                affordable, and stress-free for everyone.
              </p>
              <ul className="space-y-4">
                {[
                  "User-friendly booking process",
                  "Transparent pricing with no hidden fees",
                  "24/7 customer support",
                  "Regular fleet maintenance and updates",
                ].map((item, index) => (
                  <motion.li
                    key={index}
                    initial={{ opacity: 0, x: -20 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.1 }}
                    className="flex items-center gap-2"
                  >
                    <CheckCircle className="w-5 h-5 text-orange-500 flex-shrink-0" />
                    <span className="text-gray-700">{item}</span>
                  </motion.li>
                ))}
              </ul>
            </div>
            <div className="grid grid-cols-2 gap-4">
              {stats.map((stat, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="bg-gray-50 p-6 rounded-lg text-center group hover:bg-orange-50 transition-colors"
                >
                  <h3 className="text-3xl font-bold text-orange-500 mb-2 group-hover:scale-110 transition-transform">
                    {stat.value}
                  </h3>
                  <p className="text-gray-600">{stat.label}</p>
                </motion.div>
              ))}
            </div>
          </motion.div>
        </div>
      </section>

      {/* Basic Features Section */}
      <section className="py-16">
        <div className="container mx-auto px-4">
          <motion.div
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <div className="flex items-center justify-center gap-2 mb-4">
              <Settings className="w-6 h-6 text-orange-500" />
              <h2 className="text-3xl font-bold">Key Features</h2>
            </div>
            <p className="text-gray-600 max-w-2xl mx-auto">
              Discover what makes us the preferred choice for car rentals
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
            {featureCards.map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
                className={`${feature.bgColor} rounded-lg p-6 hover:scale-105 transition-transform`}
              >
                <feature.icon className={`w-8 h-8 ${feature.color} mb-4`} />
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </motion.div>
            ))}
          </div>

          {/* Advanced Features */}
          <motion.div
            variants={fadeIn}
            initial="initial"
            whileInView="whileInView"
            viewport={{ once: true }}
            className="mt-20"
          >
            <div className="text-center mb-12">
              <h3 className="text-2xl font-bold mb-4">Advanced Features</h3>
              <p className="text-gray-600 max-w-2xl mx-auto">
                Our application is packed with powerful features to ensure a
                smooth car rental experience
              </p>
            </div>

            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
              {advancedFeatures.map((feature, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                  className="bg-white rounded-xl p-6 border border-gray-100 hover:border-orange-200 
                           transition-all hover:-translate-y-1 group"
                >
                  <div
                    className={`${feature.bgColor} w-12 h-12 rounded-lg flex items-center justify-center 
                                mb-4 group-hover:scale-110 transition-transform`}
                  >
                    <feature.icon className={`w-6 h-6 ${feature.color}`} />
                  </div>
                  <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                  <p className="text-gray-600">{feature.description}</p>
                </motion.div>
              ))}
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
};

export default About;


================================================
FILE: frontend/src/components/StartForm.tsx
================================================
'use client';

import { useState, ChangeEvent, FormEvent } from 'react';
import { AlertCircle, Loader2 } from 'lucide-react';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

interface Sector {
  name: string;
  icon: string;
}

interface FormData {
  companyName: string;
  companyDescription: string;
  companySector: string;
  location: string;
}

interface SeoResponse {
  company_name: string;
  seo_keywords: string[];
}

interface CompanyName {
  name: string;
  rationale: string;
}

interface TaglineResponse {
  response: {
    company_names: CompanyName[];
  };
}

interface Results {
  companyName: string;
  keywords: string[];
  taglines: CompanyName[];
}

const sectors: Sector[] = [
  { name: 'Healthcare', icon: '💉' },
  { name: 'Finance', icon: '💰' },
  { name: 'Technology', icon: '💻' },
  { name: 'Retail', icon: '🛍️' },
  { name: 'Education', icon: '📚' },
  { name: 'Real Estate', icon: '🏠' },
  { name: 'Entertainment', icon: '🎬' },
  { name: 'Hospitality', icon: '🏨' },
];

const API_BASE_URL = 'https://dotslash-backend.onrender.com';

const SeoGenerator: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    companyName: '',
    companyDescription: '',
    companySector: '',
    location: '',
  });
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
  const [results, setResults] = useState<Results | null>(null);

  const handleInputChange = (
    e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ): void => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSectorClick = (sectorName: string): void => {
    setFormData(prev => ({ ...prev, companySector: sectorName }));
  };

  const fetchSeoKeywords = async (): Promise<SeoResponse> => {
    const params = new URLSearchParams({
      company_description: formData.companyDescription,
      location: formData.location
    });
    
    const response = await fetch(`${API_BASE_URL}/seo?${params}`);
    
    if (!response.ok) {
      throw new Error('Failed to fetch SEO keywords');
    }

    const data = await response.json();
    if (!data || !data.seo_keywords) {
      throw new Error('Invalid SEO response format');
    }
    return data;
  };

  const fetchTaglines = async (): Promise<CompanyName[]> => {
    const payload = {
      company_description: formData.companyDescription,
      company_sector: formData.companySector
    };

    const response = await fetch(`${API_BASE_URL}/tagline-generator`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      throw new Error('Failed to fetch taglines');
    }

    const data: TaglineResponse = await response.json();
    return data.response.company_names || [];
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>): Promise<void> => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResults(null);

    try {
      const [seoResponse, taglines] = await Promise.all([
        fetchSeoKeywords(),
        fetchTaglines()
      ]);

      setResults({
        companyName: seoResponse.company_name || formData.companyName,
        keywords: seoResponse.seo_keywords || [],
        taglines: taglines || []
      });
    } catch (err) {
      setError('Failed to generate content. Please try again.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const renderResults = () => {
    if (!results) return null;
  
    return (
      <div className="space-y-6">
        {results.keywords && results.keywords.length > 0 && (
          <div>
            <h3 className="font-semibold text-lg mb-2">SEO Keywords</h3>
            <div className="flex flex-wrap gap-2">
              {results.keywords.map((keyword, idx) => (
                <span key={idx} className="px-3 py-1 bg-orange-100 text-orange-800 rounded-full text-sm">
                  {keyword}
                </span>
              ))}
            </div>
          </div>
        )}
        
        {results.taglines && results.taglines.length > 0 && (
          <div>
            <h3 className="font-semibold text-lg mb-3">Suggested Taglines</h3>
            <div className="grid gap-3">
              {results.taglines.map((item, idx) => (
                <div key={idx} className="bg-white rounded-lg p-4 shadow-sm border border-orange-100 hover:border-orange-300 transition-colors">
                  <p className="text-gray-600 text-sm">{item.rationale}</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="container mx-auto p-4 max-w-4xl pt-24">
      <Card className="bg-white shadow-xl">
        <CardHeader className="text-center pb-2">
          <CardTitle className="text-3xl font-bold bg-gradient-to-r from-orange-500 to-pink-500 bg-clip-text text-transparent">
            SEO & Company Name Generator
          </CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="grid md:grid-cols-2 gap-4">
              {/* Input Section */}
              <div className="space-y-4">
                <input
                  type="text"
                  name="companyName"
                  value={formData.companyName}
                  onChange={handleInputChange}
                  placeholder="Company Name"
                  className="w-full px-4 py-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent"
                  required
                />
                
                <textarea
                  name="companyDescription"
                  value={formData.companyDescription}
                  onChange={handleInputChange}
                  placeholder="Describe your company..."
                  className="w-full px-4 py-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent"
                  rows={3}
                  required
                />

                <input
                  type="text"
                  name="location"
                  value={formData.location}
                  onChange={handleInputChange}
                  placeholder="Location (e.g., Surat)"
                  className="w-full px-4 py-2 rounded-lg border border-gray-200 focus:ring-2 focus:ring-orange-500 focus:border-transparent"
                  required
                />

                <div className="grid grid-cols-2 gap-2">
                  {sectors.map((sector) => (
                    <button
                      key={sector.name}
                      type="button"
                      onClick={() => handleSectorClick(sector.name)}
                      className={`p-2 rounded-lg text-sm transition-all ${
                        formData.companySector === sector.name
                          ? 'bg-orange-500 text-white shadow-md'
                          : 'bg-gray-100 hover:bg-gray-200'
                      }`}
                    >
                      <span className="text-xl block mb-1">{sector.icon}</span>
                      {sector.name}
                    </button>
                  ))}
                </div>

                <button
                  type="submit"
                  disabled={loading || !formData.companyDescription || !formData.companySector || !formData.location}
                  className="w-full py-2 px-4 bg-orange-500 text-white rounded-lg hover:bg-orange-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                >
                  {loading ? (
                    <span className="flex items-center justify-center">
                      <Loader2 className="animate-spin mr-2" size={18} />
                      Generating...
                    </span>
                  ) : (
                    'Generate Content'
                  )}
                </button>
              </div>

              {/* Results Section */}
              <div className="bg-gray-50 rounded-lg p-4">
                {error && (
                  <Alert variant="destructive">
                    <AlertCircle className="h-4 w-4" />
                    <AlertDescription>{error}</AlertDescription>
                  </Alert>
                )}
                
                {!error && !loading && results && renderResults()}

                {!error && !loading && !results && (
                  <div className="text-center text-gray-500 py-8">
                    Enter your company details to generate SEO keywords and company names
                  </div>
                )}
              </div>
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default SeoGenerator;


================================================
FILE: frontend/src/components/SWOTAnaylis.tsx
================================================
'use client';
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";

interface SWOTData {
  strengths: string[];
  weaknesses: string[];
  opportunities: string[];
  threats: string[];
}

const SWOTAnalysis = ({ swotData }: { swotData: SWOTData }) => (
  <div className="lg:w-2/3 w-full animate-slide-in-right">
    <div className="grid md:grid-cols-2 gap-6">
      {[
        {
          title: "Strengths",
          color: "from-green-50 to-green-100",
          textColor: "text-green-800",
          items: swotData.strengths,
        },
        {
          title: "Weaknesses",
          color: "from-red-50 to-red-100",
          textColor: "text-red-800",
          items: swotData.weaknesses,
        },
        {
          title: "Opportunities",
          color: "from-blue-50 to-blue-100",
          textColor: "text-blue-800",
          items: swotData.opportunities,
        },
        {
          title: "Threats",
          color: "from-yellow-50 to-yellow-100",
          textColor: "text-yellow-800",
          items: swotData.threats,
        },
      ].map((section, index) => (
        <Card
          key={index}
          className={`transform hover:scale-105 transition-all duration-300 shadow-lg bg-gradient-to-br ${section.color} hover:shadow-xl`}
          style={{ animationDelay: `${index * 150}ms` }}
        >
          <CardHeader className="p-4">
            <CardTitle className={`text-xl font-bold flex items-center gap-3 ${section.textColor}`}>
              {section.title}
            </CardTitle>
          </CardHeader>
          <CardContent className="p-4">
            <ul className="space-y-3">
              {section.items.map((item, itemIndex) => (
                <li key={itemIndex} className="flex items-center gap-2 group">
                  <div className={`w-2 h-2 rounded-full bg-${section.textColor.split("-")[1]}-500`}></div>
                  <span className={`${section.textColor} transform group-hover:translate-x-2 transition-transform`}>
                    {item}
                  </span>
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      ))}
    </div>
  </div>
);

export default SWOTAnalysis;


================================================
FILE: frontend/src/components/Team.tsx
================================================
'use client'
import React, { useState } from 'react';
import { Mail, Linkedin, Instagram } from 'lucide-react';
import Image from 'next/image';

const teamMembers = [
  {
    name: "Lakshit Vedant",
    college: "College Name",
    year: "3rd Year",
    branch: "Computer Science",
    role: "Frontend Developer",
    image: "/2.svg",
    linkedin: "https://www.linkedin.com/in/lakshit-vedant/",
    email: "mailto:email@example.com",
    instagram: "https://instagram.com/username"
  },
  {
    name: "Team Member 2",
    college: "College Name",
    year: "3rd Year",
    branch: "Computer Science",
    role: "Frontend Developer",
    image: "/2.svg",
    linkedin: "https://linkedin.com",
    email: "mailto:email@example.com",
    instagram: "https://instagram.com"
  },
  {
    name: "Team Member 3",
    college: "College Name",
    year: "3rd Year",
    branch: "Computer Science",
    role: "Frontend Developer",
    image: "/2.svg",
    linkedin: "https://linkedin.com",
    email: "mailto:email@example.com",
    instagram: "https://instagram.com"
  }
];

const Team = () => {
  const [hoveredIndex, setHoveredIndex] = useState<number | null>(null);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-red-100">
      <h1 className="text-center text-6xl pt-10 font-bold max-sm:text-4xl">
        Team Members
      </h1>
      
      <div className="flex justify-center items-center gap-8 h-[80vh] max-sm:block p-3">
        {teamMembers.map((member, index) => (
          <div
            key={index}
            className="group relative"
            onMouseEnter={() => setHoveredIndex(index)}
            onMouseLeave={() => setHoveredIndex(null)}
          >
            <Image
              src={member.image}
              alt={member.name}
              className="w-[450px] h-[450px] transition-all duration-500 group-hover:scale-110"
            />
            
            {hoveredIndex === index && (
              <div className="absolute top-1/2 left-full -translate-y-1/2 ml-4 bg-black/80 text-white p-6 rounded-lg w-64 transition-all duration-300 z-10">
                <h2 className="text-2xl font-bold mb-2">{member.name}</h2>
                <p className="text-lg mb-1">{member.college}</p>
                <p className="mb-1">{member.year} - {member.branch}</p>
                <p className="mb-4">{member.role}</p>
                
                <div className="flex gap-4">
                  <a
                    href={member.linkedin}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:text-blue-400 transition-colors"
                  >
                    <Linkedin size={24} />
                  </a>
                  <a
                    href={member.email}
                    className="hover:text-blue-400 transition-colors"
                  >
                    <Mail size={24} />
                  </a>
                  <a
                    href={member.instagram}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="hover:text-pink-400 transition-colors"
                  >
                    <Instagram size={24} />
                  </a>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Team;


================================================
FILE: frontend/src/components/Work.tsx
================================================
'use client';

import React from "react";
import { motion } from "framer-motion";
import {
  Search, // Icon for search
  Lightbulb, // Icon for insights
  ShieldCheck, // Icon for strengths,   // Icon for weaknesses
  Users,       // Icon for competitors,
  CheckCircle,
  CircleHelp,     // Icon for location
} from "lucide-react";

interface Step {
  icon: React.ComponentType<{ className?: string }>;
  title: string;
  description: string;
  bgcolor: string;
  iconcolor: string;
}

const Work = () => {
  const container = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: {
        staggerChildren: 0.2,
      },
    },
  };

  const item = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0 },
  };

  const steps: Step[] = [
    {
      icon: Search,
      title: "Company Research & Competitor Analysis",
      description:
        "Conduct in-depth company research, competitor analysis, and SWOT analysis using just the company name and location—regardless of its size. Get valuable SEO keywords for strategic growth.",
      bgcolor: "bg-blue-50",
      iconcolor: "text-blue-500",
    },
    {
      icon: Users,
      title: "Build Your Business",
      description:
        "Generate a unique company name and tagline, and connect with incubation cells directly through our platform to accelerate your startup journey.",
      bgcolor: "bg-green-50",
      iconcolor: "text-green-500",
    },
    {
      icon: ShieldCheck,
      title: "Pretrained Sector Models",
      description: "Access AI-powered chatbots and fraud detection systems tailored for healthcare, finance, legal, and e-commerce. Our solutions include medical bots for general medical queries and health insurance fraud detection.",
      bgcolor: "bg-purple-50",
      iconcolor: "text-purple-500",
    },
    {
      icon: Lightbulb,
      title: "Marketing Bot & Strategy",
      description: "Leverage AI-driven marketing bots for customized marketing strategies. We provide solutions for large-scale user engagement, competition analysis, and sector-based services to optimize your business growth.",
      bgcolor: "bg-orange-50",
      iconcolor: "text-orange-500",
    },
  ];

  return (
    <section className="py-2 bg-white">
      <div className="container mx-auto px-4">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center max-w-3xl mx-auto mb-16"
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-orange-100 rounded-full mb-4">
            <CircleHelp className="w-5 h-5 text-orange-500" />
            <span className="text-orange-700 font-medium">Who we are?</span>
          </div>
          <h2 className="text-5xl font-bold mb-6 mt-2">
            We are AIaaS!
          </h2>
          <p className="text-gray-600 text-3xl leading-relaxed">
            Research, Strategy & Growth in One Platform

          </p>
        </motion.div>

        <motion.div
          variants={container}
          initial="hidden"
          whileInView="show"
          viewport={{ once: true }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8"
        >
          {steps.map((step, index) => (
            <motion.div key={index} variants={item} className="relative group">
              <div
                className={`${step.bgcolor} rounded-xl p-8 h-full transition-all duration-300 
                           group-hover:shadow-xl group-hover:-translate-y-2`}
              >
                <div className="flex flex-col items-center text-center">
                  <div
                    className={`w-16 h-16 ${step.bgcolor} rounded-full flex items-center 
                               justify-center mb-6 group-hover:scale-110 transition-transform`}
                  >
                    <step.icon className={`w-10 h-10 ${step.iconcolor}`} />
                  </div>
                  <h3 className="text-xl font-semibold mb-4">{step.title}</h3>
                  <p className="text-gray-600 leading-relaxed">
                    {step.description}
                  </p>

                  <div
                    className="absolute -top-4 -right-4 w-8 h-8 bg-orange-500 rounded-full 
                              flex items-center justify-center text-white font-bold"
                  >
                    {index + 1}
                  </div>
                </div>

                {index !== steps.length - 1 && (
                  <div
                    className="hidden lg:block absolute top-1/2 left-full w-8 border-t-2 
                               border-dashed border-orange-300 -translate-y-1/2 z-10"
                  ></div>
                )}
              </div>

              <div className="absolute bottom-4 right-4">
                <CheckCircle
                  className="w-6 h-6 text-gray-300 group-hover:text-green-500 
                                   transition-colors"
                />
              </div>
            </motion.div>
          ))}
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mt-16 text-center"
        >
          <p className="text-gray-600 mb-6">
            Ready to unlock your AI world?
          </p>
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="px-8 py-4 bg-orange-500 text-white rounded-lg shadow-lg 
                     shadow-orange-500/30 hover:bg-orange-600 transition-all"
          >
            Get Started Now
          </motion.button>
        </motion.div>
      </div>
    </section>
  );
};

export default Work;


================================================
FILE: frontend/src/components/ui/alert.tsx
================================================
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const alertVariants = cva(
  "relative w-full rounded-lg border px-4 py-3 text-sm [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4 [&>svg]:text-foreground [&>svg~*]:pl-7",
  {
    variants: {
      variant: {
        default: "bg-background text-foreground",
        destructive:
          "border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

const Alert = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & VariantProps<typeof alertVariants>
>(({ className, variant, ...props }, ref) => (
  <div
    ref={ref}
    role="alert"
    className={cn(alertVariants({ variant }), className)}
    {...props}
  />
))
Alert.displayName = "Alert"

const AlertTitle = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLHeadingElement>
>(({ className, ...props }, ref) => (
  <h5
    ref={ref}
    className={cn("mb-1 font-medium leading-none tracking-tight", className)}
    {...props}
  />
))
AlertTitle.displayName = "AlertTitle"

const AlertDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm [&_p]:leading-relaxed", className)}
    {...props}
  />
))
AlertDescription.displayName = "AlertDescription"

export { Alert, AlertTitle, AlertDescription }



================================================
FILE: frontend/src/components/ui/button.tsx
================================================
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        default:
          "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline:
          "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }



================================================
FILE: frontend/src/components/ui/card.tsx
================================================
import * as React from "react"

import { cn } from "@/lib/utils"

const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-xl border bg-card text-card-foreground shadow",
      className
    )}
    {...props}
  />
))
Card.displayName = "Card"

const CardHeader = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 p-6", className)}
    {...props}
  />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("font-semibold leading-none tracking-tight", className)}
    {...props}
  />
))
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex items-center p-6 pt-0", className)}
    {...props}
  />
))
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }



================================================
FILE: frontend/src/components/ui/input.tsx
================================================
import * as React from "react"

import { cn } from "@/lib/utils"

const Input = React.forwardRef<HTMLInputElement, React.ComponentProps<"input">>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          "flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Input.displayName = "Input"

export { Input }



================================================
FILE: frontend/src/components/ui/label.tsx
================================================
"use client"

import * as React from "react"
import * as LabelPrimitive from "@radix-ui/react-label"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const labelVariants = cva(
  "text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
)

const Label = React.forwardRef<
  React.ElementRef<typeof LabelPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof LabelPrimitive.Root> &
    VariantProps<typeof labelVariants>
>(({ className, ...props }, ref) => (
  <LabelPrimitive.Root
    ref={ref}
    className={cn(labelVariants(), className)}
    {...props}
  />
))
Label.displayName = LabelPrimitive.Root.displayName

export { Label }



================================================
FILE: frontend/src/components/ui/scroll-area.tsx
================================================
"use client"

import * as React from "react"
import * as ScrollAreaPrimitive from "@radix-ui/react-scroll-area"

import { cn } from "@/lib/utils"

const ScrollArea = React.forwardRef<
  React.ElementRef<typeof ScrollAreaPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.Root>
>(({ className, children, ...props }, ref) => (
  <ScrollAreaPrimitive.Root
    ref={ref}
    className={cn("relative overflow-hidden", className)}
    {...props}
  >
    <ScrollAreaPrimitive.Viewport className="h-full w-full rounded-[inherit]">
      {children}
    </ScrollAreaPrimitive.Viewport>
    <ScrollBar />
    <ScrollAreaPrimitive.Corner />
  </ScrollAreaPrimitive.Root>
))
ScrollArea.displayName = ScrollAreaPrimitive.Root.displayName

const ScrollBar = React.forwardRef<
  React.ElementRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>,
  React.ComponentPropsWithoutRef<typeof ScrollAreaPrimitive.ScrollAreaScrollbar>
>(({ className, orientation = "vertical", ...props }, ref) => (
  <ScrollAreaPrimitive.ScrollAreaScrollbar
    ref={ref}
    orientation={orientation}
    className={cn(
      "flex touch-none select-none transition-colors",
      orientation === "vertical" &&
        "h-full w-2.5 border-l border-l-transparent p-[1px]",
      orientation === "horizontal" &&
        "h-2.5 flex-col border-t border-t-transparent p-[1px]",
      className
    )}
    {...props}
  >
    <ScrollAreaPrimitive.ScrollAreaThumb className="relative flex-1 rounded-full bg-border" />
  </ScrollAreaPrimitive.ScrollAreaScrollbar>
))
ScrollBar.displayName = ScrollAreaPrimitive.ScrollAreaScrollbar.displayName

export { ScrollArea, ScrollBar }



================================================
FILE: frontend/src/hooks/sendMail.tsx
================================================
"use server";
import { compileWelcomeTemplate, sendMail } from "@/lib/mail";

type Props = {
	name: string;
	email: string;
	message: string;
};

const send = async ({ name, email, message }: Props) => {
	await sendMail({
		to: "mjgandhi2305@gmail.com",
		name: name,
		subject: `Response From ${name}`,
		body: compileWelcomeTemplate(name, email, message),
	});
};

export default send;



================================================
FILE: frontend/src/lib/firebase.ts
================================================
import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, GithubAuthProvider } from "firebase/auth";

// Your Firebase configuration
const firebaseConfig = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const googleProvider = new GoogleAuthProvider();
const githubProvider = new GithubAuthProvider();

export { auth, googleProvider, githubProvider };



================================================
FILE: frontend/src/lib/mail.ts
================================================
import nodemailer from "nodemailer";
import * as handlebars from "handlebars";
import { welcomeTemplate } from "./templates/welcome";

export async function sendMail({
	to,
	subject,
	body,
}: {
	to: string;
	name: string;
	subject: string;
	body: string;
}) {
	const { SMTP_EMAIL, SMTP_PASSWORD } = process.env;

	const transport = nodemailer.createTransport({
		service: "gmail",
		secure: true,
		port: 465,
		auth: {
			user: SMTP_EMAIL,
			pass: SMTP_PASSWORD,
		},
	});
	//   try {
	//     const testResult = await transport.verify();
	//     console.log(testResult);
	//   } catch (error) {
	//     console.error({ testResult: error });
	//     return;
	//   }

	try {
		const sendResult = await transport.sendMail({
			from: SMTP_EMAIL,
			to,
			subject,
			html: body,
		});
		console.log(sendResult);
	} catch (error) {
		console.log({ sendResult: error });
	}
}

export function compileWelcomeTemplate(
	name: string,
	email: string,
	message: string
) {
	const template = handlebars.compile(welcomeTemplate);
	const htmlBody = template({
		name: name,
		message: message,
        email: email,
	});
	return htmlBody;
}



================================================
FILE: frontend/src/lib/utils.ts
================================================
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}



================================================
FILE: frontend/src/lib/templates/welcome.ts
================================================
export const welcomeTemplate = `
<!DOCTYPE html>
<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

<head>

</head>

<body>
    <h1>Hello, {{name}}! </h1>
    <p>{{message}}</p>
    <p>{{email}}</p>
</body>

</html>
`;



================================================
FILE: ml/analysis.py
================================================
import requests
from groq import Groq
import re
import json
from dotenv import load_dotenv

load_dotenv()

def companies_analysis(company_info, api_key):
    """Fetches company details using Groq AI."""
    client = Groq(api_key=api_key)

    # Create a structured prompt for the AI model
    prompt = f"""
    
    
    From the {company_info} find all the companies.
    
    Provide the following details for each companies:
    1. Official Name
    2. Strengths of Company
    3. Weakness of Company
    4. Opportunity of Company
    5. Threats to the Company
    
    Strictly always return response in JSON format as shown in example. 
    Compulsarily, find all the details of only first 3 companies.
    """

    prompt += """
    Example:
    Output:
    {
        "companies": [
            {
                "Official Name": "Challengerate",
                "Strengths of Company": "Strong e-commerce platform, diverse range of products, strategic location in Surat, India",
                "Weakness of Company": "Limited geographical presence, lack of website, intense competition in the retail industry",
                "Opportunity of Company": "Expansion into new markets, increasing demand for online shopping, potential partnerships with suppliers",
                "Threats to the Company": "Intense competition from established players, changing consumer preferences, economic downturn"
            },
            {
                "Official Name": "Reliance Retail",
                "Strengths of Company": "Strong brand reputation, wide range of products, extensive geographical presence",
                "Weakness of Company": "High operating costs, dependence on few suppliers, intense competition in the retail industry",
                "Opportunity of Company": "Expansion into new markets, increasing demand for online shopping, potential partnerships with international brands",
                "Threats to the Company": "Intense competition from e-commerce players, changing consumer preferences, regulatory challenges"
            },
            {
                "Official Name": "V-Mart Retail",
                "Strengths of Company": "Strong presence in Tier 2 and Tier 3 cities, diverse range of products, efficient supply chain management",
                "Weakness of Company": "Limited presence in metro cities, high dependence on few suppliers, intense competition in the retail industry",
                "Opportunity of Company": "Expansion into new markets, increasing demand for online shopping, potential partnerships with local suppliers",
                "Threats to the Company": "Intense competition from established players, changing consumer preferences, economic downturn"
            }
        ]
    }
    """


    # Call Groq API
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured company information."},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=500
    )

    response_content = str(completion.choices[0].message.content).strip()
    
    if not response_content:
        raise ValueError("Empty response received from Groq AI.")

    # Remove code block formatting if present
    cleaned_json = re.sub(r"```json|```", "", response_content).strip()

    try:
        print(cleaned_json)
        return json.loads(cleaned_json)  # Convert to Python dictionary
    except json.JSONDecodeError as e:
        print("Invalid JSON Response:", response_content)
        raise ValueError("Failed to parse response as JSON.") from e


================================================
FILE: ml/companies.py
================================================
from groq import Groq
import json
import re
import dotenv

dotenv.load_dotenv()

def get_company_info(company_name: str, location: str, api_key: str):
    """Fetches company details using Groq AI."""
    client = Groq(api_key=api_key)

    # Create a structured prompt for the AI model
    prompt = f"""
    Extract key details about the company based on the given prompt:
    Strictly always return response in JSON format as shown in example

    ### Instructions:
    - Ensure the JSON response is well-formed and strictly follows valid JSON syntax.
    - **Do not include unbalanced curly braces `{{}}` inside any key or value.**
    - **Do not wrap JSON in triple backticks (` ``` `).**
    - If any data is unavailable, return "Not Available" instead of leaving fields empty.
    
    Company: {company_name}
    Location: {location}
    
    Provide the following details:
    1. Official Name
    2. Industry Type
    3. Headquarters / Main Office Location
    4. Key Products / Services
    5. Website (if available)

    Write the competitors based on the same location, sector, and services.
    """

    prompt += """
    Example: 
    Input :
    {
        "company_name": "Avadh Group",
        "location": "Surat, India"
    }

    Output : 
    {
        "company": {
            "official_name": "Avadh Group",
            "industry_type": "Real Estate and Construction",
            "headquarters": "Surat, India",
            "key_products_services": [
                "Development of residential and commercial projects (apartments, villas, office spaces)",
                "Property management",
                "Interior design",
                "Construction"
            ],
            "website": "Not Available"
        },
        "competitors": [
            {
                "name": "Sangini Group",
                "industry_type": "Real Estate and Construction",
                "headquarters": "Surat, India",
                "key_products_services": [
                    "Residential and commercial real estate development"
                ]
            },
            {
                "name": "Rajhans Group",
                "industry_type": "Real Estate and Construction",
                "headquarters": "Surat, India",
                "key_products_services": [
                    "Property development",
                    "Interior design",
                    "Construction"
                ]
            },
            {
                "name": "JRD Group",
                "industry_type": "Real Estate and Construction",
                "headquarters": "Surat, India",
                "key_products_services": [
                    "Development of residential and commercial projects (apartments, villas, office spaces)"
                ]
            },
            {
                "name": "BK Jewels",
                "industry_type": "Real Estate and Construction",
                "headquarters": "Surat, India",
                "key_products_services": [
                    "Residential and commercial real estate development (apartments, villas, office spaces))"
                ]
            },
            {
                "name": "SPC Group",
                "industry_type": "Real Estate and Construction",
                "headquarters": "Surat, India",
                "key_products_services": [
                    "Property development",
                    "Interior design",
                    "Construction"
                ]
            }
        ]
    }
    """

    # Call Groq API
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured company information."},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=1000
    )

    # Extract response safely
    response_content = str(completion.choices[0].message.content).strip()
    
    if not response_content:
        raise ValueError("Empty response received from Groq AI.")

    # Remove code block formatting if present
    cleaned_json = re.sub(r"```json|```", "", response_content).strip()

    try:
        return json.loads(cleaned_json)  # Convert to Python dictionary
    except json.JSONDecodeError as e:
        print("Invalid JSON Response:", response_content)
        raise ValueError("Failed to parse response as JSON.") from e



================================================
FILE: ml/config.py
================================================
from dotenv import load_dotenv
import os
load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')


================================================
FILE: ml/requirements.txt
================================================
fastapi[all]
groq
python-dotenv
sentence-transformers
langchain
pypdf
pinecone[grpc]
langchain-pinecone
langchain-openai
langchain-experimental
langchain-pinecone
langchain-groq
langchain-community
pandas


================================================
FILE: ml/server.py
================================================
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from companies import get_company_info
from urllib.parse import unquote
from analysis import companies_analysis
from routes.chat_routes import router as chat_router
from dotenv import load_dotenv
import config
from routes.marketing_chatbot_routes import router as marketing_chatbot_router
from routes.generate_taglines import router as generate_taglines_router
from routes.seo_routes import router as seo_routes
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/home")
def read_root():
    return {
        'message': "Hello World!",
        'team': ['Vatsal', 'Miten', 'Laskhit']
    }

@app.get("/company")
def get_company_details(company: str, location: str):
    try:
        company = unquote(company)
        location = unquote(location)
        if config.GROQ_API_KEY is None:
            raise HTTPException(status_code=500, detail="API key is not set")
        company_info = get_company_info(company, location, api_key=config.GROQ_API_KEY)
        return company_info
    except Exception as e:
        return {
            "error": str(e)  # Return error message as JSON response if an exception occurs
        }

@app.post("/companies-analysis")
async def get_companies_analysis(request: Request):
    try:
        company_info = await request.json()
        if config.GROQ_API_KEY is None:
            raise HTTPException(status_code=500, detail="API key is not set")
        analysis_result = companies_analysis(company_info, api_key=config.GROQ_API_KEY)
        # print(analysis_result)
        return analysis_result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

app.include_router(chat_router)
app.include_router(marketing_chatbot_router)
app.include_router(generate_taglines_router)
app.include_router(seo_routes)


================================================
FILE: ml/chat/__init__.py
================================================
[Empty file]


================================================
FILE: ml/chat/src/__init__.py
================================================
[Empty file]


================================================
FILE: ml/chat/src/helper.py
================================================
from langchain.embeddings import HuggingFaceEmbeddings

#Download the Embeddings from HuggingFace 
def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')  #this model return 384 dimensions
    return embeddings


================================================
FILE: ml/chat/src/prompt.py
================================================


system_prompt1 = (
    "You are an assistant for question-answering medical related tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know or out of your scope. Use four sentences maximum and keep the "
    "answer not too consise and not too detailed.There should be nothing before or after the answer." 
    "\n\n"
    "{context}"
)

system_prompt2 = (
    "You are an assistant for question-answering medical related tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know or out of your scope. Use four sentences maximum and keep the "
    "answer not too consise and not too detailed.There should be nothing before or after the answer." 
    "\n\n"
    "{context}"
)


================================================
FILE: ml/routes/__init__.py
================================================
[Empty file]


================================================
FILE: ml/routes/chat_routes.py
================================================
from fastapi import APIRouter
from pydantic import BaseModel
from services.chat_service import get_chat_response

router = APIRouter()

class ChatRequest(BaseModel):
    msg: str

@router.post("/medical-bot")
async def chat(request: ChatRequest):
    response = await get_chat_response(request.msg)
    return {"response": response}


================================================
FILE: ml/routes/generate_taglines.py
================================================
from fastapi import APIRouter
from pydantic import BaseModel
from services.generate_taglines import get_company_info
import dotenv
import config

dotenv.load_dotenv()
router = APIRouter()

class ChatRequest(BaseModel):
    company_description: str
    company_sector: str

@router.post("/tagline-generator")
async def tagline(request: ChatRequest):
    response = get_company_info(request.company_description, request.company_sector, config.GROQ_API_KEY)
    return {"response": response}


================================================
FILE: ml/routes/marketing_chatbot_routes.py
================================================
from fastapi import APIRouter
from pydantic import BaseModel
from services.marketing_chatbot_service import get_chat_response

router = APIRouter()

class ChatRequest(BaseModel):
    msg: str

@router.post("/marketing-bot")
async def chat(request: ChatRequest):
    response = await get_chat_response(request.msg)
    return {"response": response}


================================================
FILE: ml/routes/seo_routes.py
================================================
from fastapi import APIRouter
from services.seo_service import get_seo

router = APIRouter()

@router.get("/seo")
async def fetch_company_info(company_description: str, location: str):
    """API to fetch company details"""
    return get_seo(company_description, location)


================================================
FILE: ml/services/__init__.py
================================================
[Empty file]


================================================
FILE: ml/services/chat_service.py
================================================
import os
import re
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from chat.src.helper import download_hugging_face_embeddings
from chat.src.prompt import system_prompt1

def get_response(msg: str) -> str:
    load_dotenv()

    PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

    os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY

    # Initialize embeddings and chain
    embeddings = download_hugging_face_embeddings()
    index_name = "chatbot1"

    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )

    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    llm = ChatGroq(api_key=GROQ_API_KEY, model_name="deepseek-r1-distill-llama-70b")
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt1),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    response = rag_chain.invoke({"input": msg})
    return response["answer"]


async def get_chat_response(msg: str) -> str:
    answer = str(get_response(msg))
    # Remove think tags from response
    cleaned_response = re.sub(r"<think>.*?</think>\s*", "", answer, flags=re.DOTALL)
    return cleaned_response


================================================
FILE: ml/services/generate_taglines.py
================================================
from groq import Groq
from dotenv import load_dotenv
import config
import json
import re
load_dotenv()

def get_company_info(company_description: str, company_sector: str, api_key: str):
    """Fetches company details using Groq AI."""
    client = Groq(api_key=api_key)

    # Create a structured prompt for the AI model
    prompt = f"""
    You are a specialized naming consultant for businesses. Create exactly 5 unique and memorable company names based on the following:

    INPUTS NEEDED:
    1. Company description: {company_description}
    2. Industry/sector: {company_sector}

    REQUIREMENTS:
    - Generate exactly 5 names
    - Each name should be maximum 2-3 words
    - Include a brief rationale (max 15 words) explaining each name
    - Names should be:
    * Memorable and distinct
    * Available as .com domains
    * Easy to pronounce
    * Reflective of company values
    * Relevant to industry

    ### Instructions:
    - Ensure the JSON response is well-formed and strictly follows valid JSON syntax.
    - **Do not include unbalanced curly braces `{{}}` inside any key or value.**
    - **Do not wrap JSON in triple backticks (` ``` `).**
    - If any data is unavailable, return "Not Available" instead of leaving fields empty.
    - Strictly always return response in JSON format as shown in example.

    OUTPUT FORMAT:
    Return response strictly in this JSON format:

    """
    prompt += """
    EXAMPLE:
    INPUT:
    {
    "company_description": "We are company selling competition analysis and AI-a-a-s company",
    "company_sector": "Artificial Intelligence"
    }

    OUTPUT:
    {
    "company_names": [
            {
                "name": "AIAlyze",
                "TagLine": "Analyzing AI with precision"
            },
            {
                "name": "Intellex",
                "TagLine": "Intelligent analysis solutions"
            },
            {
                "name": "CompeteAI",
                "TagLine": "Competitive edge through AI"
            },
            {
                "name": "PulseAI",
                "TagLine": "Pulsing with AI insights"
            },
            {
                "name": "Cerebro",
                "TagLine": "Brainpower for business"
            }
        ]
    }
    """

    # Call Groq API
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured company information."},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=500
    )
    response_content = str(completion.choices[0].message.content).strip()
    
    if not response_content:
        raise ValueError("Empty response received from Groq AI.")

    # Remove code block formatting if present
    cleaned_json = re.sub(r"```json|```", "", response_content).strip()

    try:
        print(cleaned_json)
        return json.loads(cleaned_json)  # Convert to Python dictionary
    except json.JSONDecodeError as e:
        print("Invalid JSON Response:", response_content)
        raise ValueError("Failed to parse response as JSON.") from e


================================================
FILE: ml/services/marketing_chatbot_service.py
================================================
import os
import re
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from chat.src.helper import download_hugging_face_embeddings
from chat.src.prompt import system_prompt2

def get_response(msg: str) -> str:
    load_dotenv()

    PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

    os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY

    # Initialize embeddings and chain
    embeddings = download_hugging_face_embeddings()
    index_name = "chatbot2"

    docsearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )

    retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    llm = ChatGroq(api_key=GROQ_API_KEY, model_name="deepseek-r1-distill-llama-70b")
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt2),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    response = rag_chain.invoke({"input": msg})
    return response["answer"]


async def get_chat_response(msg: str) -> str:
    answer = str(get_response(msg))
    # Remove think tags from response
    cleaned_response = re.sub(r"<think>.*?</think>\s*", "", answer, flags=re.DOTALL)
    return cleaned_response


================================================
FILE: ml/services/seo_service.py
================================================
from groq import Groq
from dotenv import load_dotenv
import config
import json
import re

load_dotenv()

def get_company_info(company_name: str, location: str, api_key: str):
    """Fetches company details using Groq AI."""
    client = Groq(api_key=api_key)

    # Create a structured prompt for the AI model
    prompt = f"""    
    Company: {company_name}
    Location: {location}
    
    Provide the following details:
    1. Official Name
    2. Industry Type
    3. Headquarters / Main Office Location
    4. Key Products / Services
    5. Website (if available)
    
    Write the 3 competitiors based on the same location, sector and services

    Strictly always return response in JSON format as shown in example
    """


    # Call Groq API
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured company information."},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=500
    )

    # Extract response
    return completion.choices[0].message.content

def get_seo_info(company_info: str, api_key: str):
    """Fetches company details using Groq AI."""
    client = Groq(api_key=api_key)

    # Create a structured prompt for the AI model
    prompt = f"""
    From the {company_info} the companies.

    Provide the following details for only the given company in input:
    1. 10 SEO Keywords    
    Only give the the company name and SEO keywords
    Strictly always return response in JSON format as shown in example. 
    Compulsarily find all the details for all the companies
    """


    # Call Groq API
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured company information."},
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        max_tokens=500
    )

    # Extract response
    response_content = str(completion.choices[0].message.content).strip()
    
    if not response_content:
        raise ValueError("Empty response received from Groq AI.")

    # Remove code block formatting if present
    cleaned_json = re.sub(r"```json|```", "", response_content).strip()

    try:
        print(cleaned_json)
        return json.loads(cleaned_json)  # Convert to Python dictionary
    except json.JSONDecodeError as e:
        print("Invalid JSON Response:", response_content)
        raise ValueError("Failed to parse response as JSON.") from e

def get_seo(company_description: str, location: str):
    company_info = get_company_info(company_description, location, api_key=config.GROQ_API_KEY)
    return get_seo_info(str(company_info), api_key=config.GROQ_API_KEY)


