import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
import { fileURLToPath } from 'node:url';
import { resolve, dirname } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const skillsBase = resolve(__dirname, '../../claude-code-plugin/skills');

const skills = defineCollection({
  loader: glob({ pattern: '**/SKILL.md', base: skillsBase }),
  schema: z.object({
    name: z.string(),
    description: z.string(),
    context: z.string().optional(),
  }),
});

export const collections = { skills };
