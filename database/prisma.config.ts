// Prisma 7 moved CLI configuration out of package.json into this file, and the
// datasource URL out of schema.prisma into the `datasource` block below.
// The "prisma": { "seed": ... } key in package.json is no longer read.
import { defineConfig, env } from 'prisma/config'

export default defineConfig({
  schema: 'prisma/schema.prisma',
  migrations: {
    path: 'prisma/migrations',
    seed: 'tsx prisma/seed.ts',
  },
  datasource: {
    // Resolved eagerly: every Prisma CLI command, `generate` included, needs
    // DATABASE_URL to be set. That is why the image generates the client at
    // container start rather than at build time.
    url: env('DATABASE_URL'),
  },
})
