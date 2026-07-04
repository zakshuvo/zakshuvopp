# Cursor IDE Setup — Claude Code & Codex Integration

## Tools Installed

- **Cursor IDE** — downloaded and installed from [cursor.com](https://cursor.com/), running on free plan
- **Claude Code** (Cursor extension) — installed via the Extensions/Marketplace panel
- **Codex** (Cursor extension) — installed via the Extensions/Marketplace panel
- **GitHub account** — used to host this repository

## Steps Completed

1. Downloaded and installed Cursor IDE.
2. Opened Cursor and located the Extensions panel, also labeled **"Marketplace"** in Cursor's UI (`Ctrl + Shift + X`).
3. Searched for "Claude Code" in the Marketplace, installed it, and signed in with my Claude account (free plan).
4. Searched for "Codex" in the Marketplace, installed it, and signed in with my OpenAI account.
5. Created a public GitHub repository to host this project.
6. Opened the repository in Cursor.
7. Created this README.md to document the process.
8. Committed and pushed the changes to GitHub.

## Issues Encountered & Solutions

- **Issue:** Initially went to Cursor's **Settings → General** page looking for extensions, which only shows account/billing/notification options, not the extension marketplace.
  **Solution:** Found the correct location — the **Extensions / Marketplace panel**, accessed via the puzzle-piece icon in the left sidebar or the `Ctrl + Shift + X` shortcut. This is where "Claude Code" and "Codex" can be searched and installed.

- **Issue:** Was unsure whether the free Cursor plan would support the Claude Code and Codex extensions.
  **Solution:** Confirmed the free plan is sufficient for basic use of both extensions; only heavier usage may run into rate limits.

## Notes

- Cursor is built on a VS Code-style architecture, so its Extensions panel functions the same way as VS Code's, just labeled "Marketplace" in some views.
- Claude Code requires an Anthropic/Claude account login; Codex requires a separate OpenAI account login.

---

# Research Project: AI-Powered SEO Content Production

Research phase for a future playbook on how B2B SaaS teams actually use AI to
produce SEO content — grounded in what real practitioners do, not vendor
marketing.

## Why this topic

Of several candidate topics, this one was chosen because the entire research
process is executable through public, non-login-walled sources (web search +
article/blog content). Topics like LinkedIn organic strategy or cold outreach
require login-walled scraping or contact-data tools that are either against
platform ToS or require paid infrastructure this project doesn't have yet.

## What's in `/research`

```
research/
  sources.md                    <- the 10 vetted experts: who, why, links
  linkedin-posts/<author>/      <- one file per collected post (manual collection)
  youtube-transcripts/<author>/ <- one file per collected video transcript
  other/                        <- supporting case studies / background data
scripts/
  fetch_youtube_transcripts.py  <- pulls captions via youtube-transcript-api (free) or Supadata
  linkedin_post_template.md     <- template + instructions for manual LinkedIn collection
  requirements.txt
```

## How the 10 experts were chosen

An initial broad search ("AI-powered SEO content production case studies")
mostly surfaced SEO-tool vendor blogs and agency listicles — useful for
*discovering* names, but useless as sources themselves (self-reported,
unverifiable growth claims). A second, targeted search focused on named
individuals with a real operating history: people running SEO/content at an
actual product company, or with a multi-year public research record
predating the current AI-content hype cycle.

Final list (full detail + links in `research/sources.md`):

1. **Kevin Indig** — growth advisor (ex-Shopify/Atlassian/Ramp), Growth Memo newsletter
2. **Eli Schwartz** — SEO advisor (Shutterstock, Mixpanel), author, Contrarian Marketing podcast
3. **Ryan Law** — Director of Content, Ahrefs — runs Ahrefs' own content ops
4. **Garrett Sussman** — iPullRank, The SEO Weekly — AI editorial workflow focus
5. **Jeff Coyle** — co-founder, MarketMuse — decade-long AI content-intelligence track record
6. **Amanda Natividad** — VP Marketing, SparkToro — "zero-click marketing," anti-hype counterweight
7. **Ross Simmonds** — founder, Foundation Marketing / Distribution.ai — production + distribution
8. **Chris Long** — independent SEO researcher, original AI-search-behavior studies
9. **Cyrus Shepard** — longtime independent SEO researcher (ex-Moz), skeptic voice
10. **Craig Campbell** — 20-year SEO consultant, tactical AI-workflow integration

Explicitly excluded: pure SEO-tool marketing sites (Scalenut, WP SEO AI, generic
agency case-study round-ups) — these sell AI-SEO software, so their "results"
are vendor claims, not independent practitioner accounts. They're logged in
`research/other/supporting-case-studies.md` as background context to
fact-check against, not treated as expert sources.

## Collection method & honest limitations

- **YouTube transcripts:** `scripts/fetch_youtube_transcripts.py` uses the free
  `youtube-transcript-api` by default (no key needed, works on any captioned
  video), with an optional Supadata path for videos without captions. Needs
  live internet access to youtube.com — run locally or in Claude Code.
- **LinkedIn posts:** collected manually using `scripts/linkedin_post_template.md`.
  LinkedIn has no public read API and blocks scraping via ToS; manual collection
  is the only reliable, account-safe method at this scale.
- **Status as of this commit:** expert list and vetting are complete. Actual
  transcripts/posts are pending collection — next commits will add them
  incrementally per author, not in one batch.

## Next steps toward the playbook

1. Run the YouTube script against 3-5 recent videos per expert (where they exist).
2. Manually collect 5-10 recent LinkedIn posts per expert on this topic specifically.
3. Cross-check claims against `research/other/supporting-case-studies.md`.
4. Look for agreement/disagreement patterns across the 10 (e.g., everyone agrees
   human review is non-negotiable for YMYL content; disagreement on how much
   AI-generated first-draft is acceptable).
