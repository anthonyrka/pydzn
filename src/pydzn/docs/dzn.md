# DZN Semantic Classes


```shell
# =========================
# LAYOUT & FLEXBOX
# =========================
flex                      # display:flex
flex-col                  # flex-direction:column
items-center              # align-items:center
justify-center            # justify-content:center
text-center               # text-align:center

self-center               # align-self:center
self-start                # align-self:flex-start
self-end                  # align-self:flex-end

flex-1                    # flex:1 1 0%
grow                      # flex-grow:1
shrink-0                  # flex-shrink:0

block                     # display:block
inline-block              # display:inline-block
hidden                    # display:none
visible                   # visibility:visible
invisible                 # visibility:hidden   (keeps layout space)

grid                      # display:grid
aspect-square             # aspect-ratio:1/1


# =========================
# POSITIONING / OFFSETS
# =========================
relative                  # position:relative
absolute                  # position:absolute
fixed                     # position:fixed
sticky                    # position:sticky

top-0                     # top:0
right-0                   # right:0
bottom-0                  # bottom:0
left-0                    # left:0
inset-0                   # top:0; right:0; bottom:0; left:0

# Arbitrary offsets (bracket syntax)
top-[48px]                # top:48px


# =========================
# GRID TEMPLATE (ARBITRARY)
# =========================
grid-cols-[280px_1fr]     # grid-template-columns: 280px 1fr
grid-rows-[108px_1fr]     # grid-template-rows: 108px 1fr
# (Underscores inside [...] turn into spaces)


# =========================
# SIZING (ARBITRARY)
# =========================
w-[320px]                 # width:320px
h-[100%]                  # height:100%
h-[calc(100vh-48px)]      # height:calc(100vh - 48px)


# =========================
# SPACING: GAP / PADDING / MARGIN
# (Tokenized scale: 0,1,2,3,4,5,6,7,8,9,10,11,12,14,16,20,24,28,32)
# where 1=.25rem, 2=.5rem, 4=1rem, 16=4rem, etc.
# =========================
gap-<n>                   # gap: <token size>
gap-4                     # gap: 1rem

p-<n>                     # padding: <token size>
p-4                       # padding: 1rem
px-<n>                    # padding-left/right
py-<n>                    # padding-top/bottom

# Arbitrary spacing
p-[12px]                  # padding:12px
px-[2rem]                 # padding-left/right: 2rem
py-[8px]                  # padding-top/bottom: 8px
gap-[6px]                 # gap:6px

# Margins (tokenized)
m-<n>                     # margin: <token>
mx-<n>                    # left/right
my-<n>                    # top/bottom
mt-<n> mr-<n> mb-<n> ml-<n>  # per-side
ms-<n> me-<n>             # logical start/end

# Margins (arbitrary)
m-[12px]                  # margin:12px
mx-[auto]                 # margin-left/right:auto
my-[1rem]                 # margin-top/bottom:1rem
mt-[8px] mr-[8px] ...     # per-side arbitrary
ms-[1ch] me-[1ch]         # logical start/end arbitrary

# Auto margins shortcuts
mx-auto                   # margin-left/right:auto
ml-auto                   # margin-left:auto
mr-auto                   # margin-right:auto
ms-auto                   # margin-inline-start:auto
me-auto                   # margin-inline-end:auto

# =========================
# BORDERS: STYLE / WIDTH / COLOR
# =========================
border                    # solid; width:1px; color:subtle (default)
border-solid              # border-style:solid
border-dashed             # border-style:dashed
border-dotted             # border-style:dotted

# Width — all sides
border-0                  # border-width:0
border-2                  # border-width:2px
border-4                  # border-width:4px
border-8                  # border-width:8px

# Width — axes (DEFAULT=1px when omitted)
border-x                  # left/right width:1px
border-y                  # top/bottom width:1px
border-x-2                # left/right width:2px
border-y-4                # top/bottom width:4px

# Width — sides (DEFAULT=1px when omitted)
border-t                  # top width:1px
border-r-2                # right width:2px
border-b-4                # bottom width:4px
border-l-8                # left width:8px

# Color tokens
border-subtle             # rgba(15,23,42,.06)
border-transparent        # transparent
border-black              # black
border-white              # white
border-slate-200          # rgb(226,232,240)
border-slate-300          # rgb(203,213,225)
border-slate-400          # rgb(148,163,184)
border-blue-500           # rgb(59,130,246)
border-red-500            # rgb(239,68,68)
border-green-500          # rgb(34,197,94)

# Arbitrary width
border-[1.5px]            # border-width:1.5px


# =========================
# RADIUS (ROUNDED)
# Tokens: none(0), sm(8px), md(12px), lg(16px), xl(20px), 2xl(24px), 3xl(32px), full(9999px)
# =========================
rounded                   # border-radius:12px (md)
rounded-none              # border-radius:0
rounded-<token>           # all corners
rounded-lg                # 16px radius

# Sides
rounded-t-<token>         # top-left & top-right
rounded-r-<token>         # top-right & bottom-right
rounded-b-<token>         # bottom-right & bottom-left
rounded-l-<token>         # top-left & bottom-left

# Corners
rounded-tl-<token>        # top-left
rounded-tr-<token>        # top-right
rounded-br-<token>        # bottom-right
rounded-bl-<token>        # bottom-left

# Arbitrary
rounded-[10px]            # border-radius:10px


# =========================
# SHADOWS
# =========================
shadow-none               # none
shadow-sm                 # small (0 1px 3px rgba(0,0,0,.08))
shadow                    # medium (alias of md)
shadow-md                 # medium
shadow-lg                 # large
shadow-xl                 # extra large
shadow-2xl                # 2x large
shadow-3xl                # 3x large
shadow-inner              # inset soft shadow

# Arbitrary (underscores become spaces)
shadow-[0_4px_12px_rgba(0,0,0,.12)]


# =========================
# TEXT DECORATION
# =========================
no-underline              # text-decoration:none
underline                 # text-decoration:underline
line-through              # text-decoration:line-through
decoration-solid          # text-decoration-style:solid
decoration-dashed         # text-decoration-style:dashed
decoration-dotted         # text-decoration-style:dotted


# =========================
# COLORS (ARBITRARY)
# =========================
bg-[white]                # background:white
bg-[rgba(255,255,255,.08)]# background:rgba(...)
text-[inherit]            # color:inherit
text-[#2563eb]            # color:#2563eb


# =========================
# OVERFLOW / OVERSCROLL / SCROLLBAR
# =========================
overflow-hidden           # overflow:hidden
overflow-auto             # overflow:auto
overflow-y-auto           # overflow-y:auto
overflow-x-hidden         # overflow-x:hidden
overflow-y-hidden         # overflow-y:hidden

overscroll-auto           # overscroll-behavior:auto
overscroll-contain        # overscroll-behavior:contain
overscroll-none           # overscroll-behavior:none

scrollbar-stable          # scrollbar-gutter:stable (prevents layout shift)


# =========================
# Z-INDEX (ARBITRARY)
# =========================
z-[10]                    # z-index:10
z-[999]                   # z-index:999


# =========================
# RESPONSIVE & STATE VARIANTS
# (Prefix any class with these)
# =========================
# Responsive breakpoints: sm, md, lg  →  @media (min-width: 640/768/1024px)
sm:px-4                   # padding-left/right:1rem on >=640px
md:gap-6                  # gap:1.5rem on >=768px
lg:border-b-2             # bottom border 2px on >=1024px

# States
hover:text-[#60a5fa]      # change text color on hover
focus:bg-[rgba(15,23,42,.06)]  # change background on focus

# Combined
sm:hover:underline        # underline on hover at >=640px


# =========================
# QUICK “RECIPES” (COMMON COMBOS)
# =========================
# 1px hairline divider on bottom (modern, subtle)
border-0 border-b border-subtle border-solid

# Right divider 2px slate-300
border-0 border-r-2 border-slate-300 border-solid

# Fixed sidebar 240px wide under a 48px appbar, full viewport height
fixed top-[48px] left-0 w-[240px] h-[calc(100vh-48px)] overflow-y-auto overscroll-contain

# Full-bleed grid: sidebar 128px + main grows
grid grid-cols-[128px_1fr] grid-rows-[108px_1fr]

# Center content block, limit width, pad
mx-auto w-[min(1200px,100%)] p-8


# Spacing tokens (n → rem)
1=.25  2=.5  3=.75  4=1  5=1.25  6=1.5  7=1.75  8=2
9=2.25 10=2.5 11=2.75 12=3  14=3.5  16=4  20=5  24=6  28=7  32=8

# Radius tokens
none=0  sm=8px  md=12px  lg=16px  xl=20px  2xl=24px  3xl=32px  full=9999px

# Border width presets
DEFAULT=1px  0=0  2=2px  4=4px  8=8px

# Border color tokens
subtle=rgba(15,23,42,.06)  transparent  black  white
slate-200/300/400
blue-500  red-500  green-500
```