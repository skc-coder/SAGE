https://nextjs.org/docs

https://www.youtube.com/watch?v=vwSlYG7hFk0

# Next.js Overview

tags: #nextjs #webdev #fullstack #overview

> **What is it?** Next.js is a React framework that lets you build full-stack applications without a separate backend. The App Router (introduced recently) is the modern way to build with it.

---

## Setup

```bash
npx create-next-app@latest .
```

During setup it asks about TypeScript, ESLint, Tailwind CSS, source directory, and App Router. Go with defaults. This creates a boilerplate — first thing you do is clean out the clutter in `page.tsx` and `globals.css`.

---

## Routing & Navigation

Next.js uses **file-system based routing**. The folder structure inside `src/app/` defines your routes.

- `src/app/page.tsx` → `/`
- `src/app/posts/page.tsx` → `/posts`
- `src/app/posts/[id]/page.tsx` → `/posts/123` (dynamic route)

The `[id]` syntax is a dynamic segment. You access it inside the component via the `params` prop — `params.id`. No need to create a folder per post, one dynamic route handles all of them.

**Navigation** uses the built-in `<Link>` component instead of `<a>`. The difference is that `<Link>` does _client-side navigation_ — the browser doesn't send a new request to the server on every click. In production, Next.js also prefetches linked pages when they come into view.

---

## Layouts

`layout.tsx` is a special file that wraps all pages at its level. The root layout at `src/app/layout.tsx` is the outermost shell — every page gets rendered as `{children}` inside it. This is where you put your header, footer, and global font/metadata.

```
layout.tsx
  ├── Header
  ├── {children}   ← your actual page goes here
  └── Footer
```

You can nest layouts — a `/dashboard/layout.tsx` would only wrap dashboard pages.

---

## Metadata

Exported from any `page.tsx` or `layout.tsx`:

```ts
export const metadata = {
  title: "My App",
  description: "...",
}
```

Defined in the root layout, it applies globally. Override it on individual pages by exporting the same object from that page's file.

---

## Styling — Tailwind CSS

Tailwind is the default. Instead of writing a separate CSS class for every element, you apply utility classes inline.

```tsx
<h1 className="text-2xl font-semibold text-gray-800">Hello</h1>
```

No context switching, no inventing class names. Next.js also gives you `globals.css` for custom or global styles. Both work together.

---

## Server vs Client Components

This is a major concept introduced with the App Router.

**Server Components** (default in `app/`):

- Render only on the server
- Can fetch data directly without `useEffect`
- Don't ship their JS to the browser
- Good for: data fetching, heavy dependencies (e.g. syntax highlighters, ORMs)

**Client Components** (add `"use client"` at top of file):

- Render in the browser
- Required for interactivity — state, effects, event handlers
- Their code and dependencies are shipped to the client

The practical implication: a syntax highlighter library that's 4MB stays on the server if the component using it is a server component. The user only receives the rendered HTML, not the library itself.

---

## Data Fetching in Server Components

In a server component you can `fetch()` directly in the function body:

```tsx
// posts/page.tsx (server component by default)
async function PostsPage() {
  const res = await fetch("https://api.example.com/posts")
  const posts = await res.json()
  return <PostList posts={posts} />
}
```

No `useEffect`, no loading state management here — it's just `async/await`. For database queries you can also call your ORM (like Prisma) directly in the component.

---

## Server Actions

This is arguably the biggest innovation. Server actions replace the old pattern of:

1. Writing an API route handler (`/api/posts`)
2. Fetching it from the client
3. Managing form state manually

Now you just write a regular function and mark it with `"use server"`:

```tsx
async function addPost(formData: FormData) {
  "use server"
  const title = formData.get("title")
  await db.post.create({ data: { title } })
  revalidatePath("/posts")
}

// In your component:
<form action={addPost}>
  <input name="title" />
  <button type="submit">Add</button>
</form>
```

Next.js handles sending the form data from client to server automatically. `revalidatePath` tells Next.js to re-render that route after the mutation — so the new post appears without a page refresh.

The `useFormStatus` hook (from React) gives you a `pending` boolean so you can disable the submit button while the action is running.

---

## Suspense & Streaming

When a server component is `async`, Next.js can _stream_ its output. Instead of waiting for all data to load before showing anything, you can show the rest of the page immediately and stream in the slow part when it's ready.

**`loading.tsx`** — a special file that acts as a fallback while the page's data loads. Next.js automatically wraps the page in a `<Suspense>` with this as the fallback.

For more granular control, wrap specific components in `<Suspense>` manually:

```tsx
<h1>All Posts</h1>

<Suspense fallback={<p>Loading posts...</p>}>
  <PostList />   {/* this fetches its own data */}
</Suspense>
```

Now the `<h1>` renders immediately, and the post list streams in when it's ready. Without this, the entire page would block until the data is fetched.

---

## Caching & Static vs Dynamic Rendering

Caching in Next.js is aggressive and has multiple layers. The two main ones:

**Data cache** — results of `fetch()` calls are cached on the server.

**Full route cache** — the rendered output of entire routes is cached.

**Static rendering** (default in production): Next.js runs the component once during `npm run build` and serves the cached result on every request. Fast, but stale.

**Dynamic rendering**: the component runs on every request. Enable it per-route:

```ts
export const dynamic = "force-dynamic"
```

Or per-fetch call:

```ts
fetch(url, { cache: "no-store" })           // never cache
fetch(url, { next: { revalidate: 3600 } }) // refresh every 1 hour
```

In development (`npm run dev`) everything is dynamic. The caching behavior only applies to production builds (`npm run build` + `npm run start`).

---

## Special Files in `app/`

|File|Purpose|
|---|---|
|`page.tsx`|The UI for a route|
|`layout.tsx`|Wraps children pages|
|`loading.tsx`|Shown while page data loads|
|`error.tsx`|Shown on errors|
|`not-found.tsx`|Shown when `notFound()` is called|
|`favicon.ico`|Browser tab icon|
|`robots.txt`|SEO crawl rules|

The `notFound()` function from Next.js can be called in any page to render the not-found UI — useful when a dynamic route gets a bad ID.

---

## Middleware

A `middleware.ts` file at the project root runs before every request hits the server. Most common use: auth guards.

```ts
export function middleware(request: NextRequest) {
  const isAuthenticated = false // check cookie/token here
  if (!isAuthenticated) {
    return NextResponse.redirect(new URL("/login", request.url))
  }
}

export const config = {
  matcher: ["/dashboard/:path*", "/account/:path*"],
}
```

The `matcher` config limits which routes the middleware runs on.

---

## Deployment

Two main paths:

**Static export** — generates plain HTML/CSS/JS files, hostable anywhere. You lose server features (server components, image optimization, server actions). Enable with `output: "export"` in `next.config.js`.

**Node.js server** — the default. Next.js is a Node.js app. Run `npm run build` then `npm run start`. Can host on:

- Managed platforms (Vercel, Netlify) — easiest, costs more at scale
- VPS (any cloud provider) — more control, cheaper at scale. Set up nginx to proxy traffic from port 80 → localhost:3000.

**Environment variables**: use `.env` for non-secrets (committed to git), `.env.local` for secrets (gitignored by default in new Next.js projects).

---

## Folder Structure (typical)

```
src/
  app/
    page.tsx           ← homepage
    layout.tsx         ← root layout
    posts/
      page.tsx
      [id]/
        page.tsx
    api/               ← route handlers (if needed)
public/                ← static assets
prisma/                ← if using Prisma ORM
.env
.env.local             ← secrets, gitignored
next.config.ts
```

---

## Related

- [[React Fundamentals]]
- [[Prisma ORM]]
- [[Tailwind CSS]]
- [[Web Deployment]]