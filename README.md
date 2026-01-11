# Cocobase Documentation

> **Complete, topic-based documentation for the Cocobase Backend-as-a-Service platform**

This documentation covers all features of Cocobase across all supported SDKs (JavaScript, Dart/Flutter, Go, Python) and the REST API.

## 📚 Documentation Structure

### **Getting Started**
- [Welcome](index.mdx) - Introduction to Cocobase
- [Quick Start](guides/getting-started.mdx) - Get up and running in minutes

### **Core Concepts**
- [Authentication](core-concepts/authentication.mdx) - User management and sessions
- [Collections & Documents](core-concepts/collections.mdx) - Data organization
- [Data Types](core-concepts/data-types.mdx) - Supported data types and type safety

### **Features**
- [CRUD Operations](features/crud-operations.mdx) - Create, read, update, delete
- [Query & Filtering](features/querying.mdx) - Advanced data querying
- [Real-time Updates](features/realtime.mdx) - WebSocket subscriptions
- [Relationships](features/relationships.mdx) - Document references and population
- [File Storage](features/file-storage.mdx) - Upload and manage files
- [Cloud Functions](features/cloud-functions.mdx) - Server-side logic
- [Advanced Features](features/advanced.mdx) - Batch operations, aggregations

### **Guides**
- [Best Practices](guides/best-practices.mdx) - Security, performance, optimization
- [Troubleshooting](guides/troubleshooting.mdx) - Common issues and solutions

### **Examples**
- [Complete Applications](examples/complete-apps.mdx) - Full app examples
  - Todo App
  - E-commerce Store
  - Social Media Feed
  - Chat Application

## 🎯 Key Features

### **Topic-Based Organization**
Unlike traditional SDK-specific documentation, this is organized by **topics** with multi-language tabs, making it easy to understand features regardless of your programming language.

### **Multi-Language Support**
Every code example is shown in:
- JavaScript/TypeScript
- Dart/Flutter
- Go
- Python
- HTTP/cURL

### **Comprehensive Coverage**
- 600+ code examples
- 12+ query operators documented
- 5 complete application examples
- 25+ troubleshooting scenarios
- Best practices for security and performance

## 🚀 Quick Navigation

### I want to...
- **Get started quickly** → [Getting Started](guides/getting-started.mdx)
- **Add user authentication** → [Authentication](core-concepts/authentication.mdx)
- **Store and retrieve data** → [CRUD Operations](features/crud-operations.mdx)
- **Filter and search data** → [Query & Filtering](features/querying.mdx)
- **Build real-time features** → [Real-time Updates](features/realtime.mdx)
- **Upload files** → [File Storage](features/file-storage.mdx)
- **See complete examples** → [Complete Apps](examples/complete-apps.mdx)
- **Solve a problem** → [Troubleshooting](guides/troubleshooting.mdx)

## 📖 SDK Documentation Sources

This unified documentation consolidates information from:
- `js-docs/` - JavaScript/TypeScript SDK (17 files, ~120KB)
- `flutter-doc/` - Flutter/Dart SDK (12 files, ~185KB)
- `cocobe golang/` - Go SDK (12 files, ~175KB)
- `api-docs/` - REST API (10 files, ~170KB)
- `cloud-function docs/` - Cloud Functions (8 files, ~130KB)

**Total**: 59 files, 760KB of documentation consolidated into topic-based guides.

## 🛠️ Technology Stack

This documentation is built with:
- **MDX** - Markdown with JSX components
- **Mintlify** - Documentation platform
- **Multi-language tabs** - Unified code examples
- **Interactive components** - Cards, accordions, tabs

## Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mint) to preview your documentation changes locally:

```bash
npm i -g mint
```

Run the following command at the root of your documentation, where your `mint.json` is located:

```bash
mint dev
```

View your local preview at `http://localhost:3000`.

## Publishing Changes

Install the Mintlify GitHub app from your [dashboard](https://dashboard.mintlify.com/settings/organization/github-app) to propagate changes from your repo to your deployment. Changes are deployed to production automatically after pushing to the default branch.

## 📝 Contributing

Found an error or want to improve the docs?

1. **Report issues**: [GitHub Issues](https://github.com/cocobase/docs/issues)
2. **Suggest improvements**: Open a pull request
3. **Ask questions**: [Discord Community](https://discord.gg/cocobase)

## 🔗 Links

- **Website**: [cocobase.buzz](https://cocobase.buzz)
- **Dashboard**: [cocobase.buzz/dashboard](https://cocobase.buzz/dashboard)
- **Discord**: [discord.gg/cocobase](https://discord.gg/cocobase)
- **GitHub**: [github.com/cocobase](https://github.com/cocobase)
- **Examples**: [github.com/cocobase/examples](https://github.com/cocobase/examples)

## Need Help?

### Troubleshooting
- If your dev environment isn't running: Run `mint update` to ensure you have the most recent version of the CLI.
- If a page loads as a 404: Make sure you are running in a folder with a valid `mint.json`.

### Resources
- [Mintlify documentation](https://mintlify.com/docs)
- [Cocobase Troubleshooting Guide](guides/troubleshooting.mdx)

## 📄 License

Documentation is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

**Built with ❤️ by the Cocobase team**
