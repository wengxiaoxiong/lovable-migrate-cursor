
## 🪄 Lovable Project Migration Assistant (+ Coding Agent Auto-Refactor)

[中文版本的文档](./README_zh.md)

> **Lovable auto-generated frontend projects**, want to upgrade to full-stack with database and API support?
> Just two steps: **run the script + start Coding Agent**, complete the leap from static to intelligent!

---

### 🔧 One-Line Summary

**This toolchain = script + template project + AI Agent**

Helps you migrate your `lovable` generated Vite project:

* ✅ **One-click migration** to Next.js full-stack template structure
* 🤖 **Hand over to Coding Agent**, automatically supplement API, database schema, and data integration logic
* 🚀 Quick deployment or continued development, achieving the upgrade from "toy project" to "real application"

---

### ✅ Step 1: Run Script, Complete File Migration

```bash
python migrate_lovable.py
```

The script will prompt you for the lovable project folder name, then:

| Source Path                          | Migration Action | Target Path                                      |
| ------------------------------------ | ---------------- | ------------------------------------------------ |
| `./[lovable]/public/`                | Copy             | `./next-fullstack-template/public/`                |
| `./[lovable]/src/components/`        | Move             | `./next-fullstack-template/components/`            |
| `./[lovable]/src/remaining content`  | Copy             | `./next-fullstack-template/components/app/`        |

📁 Final directory structure based on: [`next-lovable-template`](https://github.com/wengxiaoxiong/next-fullstack-template)

---

### 🔄 Step 2: Start Coding Agent, Auto-Intelligent Refactor

> After running the script, you'll get a **visually identical project structure**, but **subsequent work requires Coding Agent to complete the real "intelligent migration"**.

🎯 Coding Agent will automatically complete these tasks:

| Feature            | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| 🔍 Page Analysis   | Migrate Vite project page structure to Next.js App Router format |
| 🧠 Mock Inference | Infer database models from original mock data (e.g., User/Product/Task) |
| 🏗️ Prisma Modeling | Auto-generate `schema.prisma` and create database migrations |
| ⚙️ API Creation    | Auto-create `app/api/*` routes and logic based on business logic |
| 🧪 Local Testing   | Extensible to auto-generate test data and debug API calls |

> You just need to start Agent in VSCode or connect LLM tools, then work with Coding Agent to continuously complete refactoring!

📌 **Prompt Template Recommendations:**

Already written here
[Chinese Version PROMPT_zh.md](./next-lovable-template/PROMPT_zh.md)
[English Version PROMPT.md](./next-lovable-template/PROMPT.md)

---

### 🛠️ Step 3: Development Environment Setup

After script execution, navigate to the project directory and set up the development environment:

```bash
cd next-lovable-template

# Install dependencies
sudo pnpm install

# Start development server
pnpm dev

```

**Important Notes:**
- Use `sudo pnpm install` to ensure proper permissions
- The dev server will start at `http://localhost:3000`
- Database commands are only needed if your project uses Prisma ORM
- For production deployment, use `pnpm build` and `pnpm start`

---

### 🧰 Template Project Highlights (next-lovable-template)

* ✅ **Next.js 15 + App Router** (modern React full-stack architecture)
* ✅ **Prisma ORM** (database modeling + API data layer)
* ✅ **Vercel Blob** (file upload capabilities)
* ✅ **AI SDK** (AI functionality integration)
* ✅ **Tailwind CSS + shadcn/ui** (ultimate development experience)
* ✅ **ESLint** & `pnpm dev` ready to start

📦 Template Repository: [https://github.com/wengxiaoxiong/next-fullstack-template](https://github.com/wengxiaoxiong/next-fullstack-template)
📺 Tutorial Video: [Chinese Deployment Tutorial (Bilibili)](https://www.bilibili.com/video/BV1xW8mzTETn/)

---

### 🚀 Why This Toolchain is Worth Using?

| Traditional Approach            | Using Lovable + Agent |
| ----------------------------- | --------------------- |
| Manual page structure creation | Auto-migrate to App Router |
| Hand-write Prisma + API | Let Agent intelligently infer and generate |
| Rewrite styles + architecture alignment | Preserve original styles, intelligent structure adaptation |
| Repeated debugging, difficult deployment | Template deployment architecture, instant deployment |

---

### 🧪 Project Target Audience

* Want to upgrade lovable-generated prototype projects to real products
* Don't understand backend but want API and database capabilities
* Hope to combine Coding Agent for intelligent development, improving efficiency
* Entrepreneurs, designers, PMs, indie developers

---

### 🧠 Summary

> **lovable** is the inspiration starting point, **script** is the migration bridge, **Coding Agent** is the development partner, **template** is the deployment foundation.
> One toolchain, from 0 to 1, easily start your full-stack application journey!

[中文文档](README_zh.md)

