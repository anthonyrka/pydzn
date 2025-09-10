from pydzn.base_component import BaseComponent
from pydzn.variants import VariantSupport


class NavItem(VariantSupport, BaseComponent):
    """
    Minimal nav item with pluggable variants.
    Use `children` to supply the label (e.g., a Text component).

    Families:
      - sidebar-*: full-width tiles for sidebars
      - dropdown-*: compact rows for menus

    Examples:
      NavItem(variant="sidebar-default", children=Text("Overview").render())
      NavItem(variant="dropdown-item",  children=Text("Rename").render())

      # Discover available options:
      NavItem.list_variants()      # -> dict of variants
      NavItem.list_sizes()         # -> dict of sizes
      NavItem.list_tones()         # -> dict of tones
    """

    # ---------- Variants ----------
    VARIANTS = {
        # --- Sidebar family ---
        # Classic tile: full width, fixed height, single divider line at bottom.
        "sidebar-default": (
            "w-[100%] h-[48px] "
            "flex items-center justify-center text-center "
            "rounded-none "
            "border-solid border-b border-subtle "   # bottom divider only
            "text-body hover:bg-[rgba(15,23,42,.06)]"
        ),
        # Same but slightly taller.
        "sidebar-compact": (
            "w-[100%] h-[40px] "
            "flex items-center justify-center text-center "
            "rounded-none "
            "border-solid border-b border-subtle "
            "text-body hover:bg-[rgba(15,23,42,.06)]"
        ),
        # Selected/active look (apply explicitly where needed).
        "sidebar-active": (
            "w-[100%] h-[48px] "
            "flex items-center justify-center text-center "
            "rounded-none "
            "border-solid border-b border-subtle "
            "bg-[rgba(37,99,235,.10)] text-[#2563eb]"
        ),
        # Low-contrast, subtle text tone.
        "sidebar-quiet": (
            "w-[100%] h-[48px] "
            "flex items-center justify-center text-center "
            "rounded-none "
            "border-solid border-b border-subtle "
            "text-[rgb(100,116,139)] hover:bg-[rgba(15,23,42,.04)]"
        ),
        # NavItem.VARIANTS entry
        "sidebar-underline": (
            "w-[100%] "                       # full width of the sidebar
            "flex items-center justify-center text-center "
            "rounded-none "
            "border-0 border-b border-subtle border-solid "  # <- only bottom line
            "py-2"                            # space between text and the line
        ),

        "sidebar-squared-underline": (
            "w-[100%] h-[64px] "
            "flex items-center justify-center text-center "
            "rounded-none "
            "border-0 border-b border-subtle border-solid "
            "py-2 "
            # hovers:
            "hover:bg-[rgba(37,99,235,.06)] "   # soft blue wash on hover
            "hover:border-blue-500 "            # underline turns blue
            "hover:text-[#2563eb] "             # text turns blue
            # optional focus (keyboard users):
            "focus:bg-[rgba(37,99,235,.10)] "
        ),


        # --- Dropdown family ---
        # Menu row: no borders, small padding, hover tint.
        "dropdown-item": (
            "w-[100%] px-3 py-2 "
            "rounded-md border-0 "
            "bg-[transparent] text-body "
            "hover:bg-[rgba(15,23,42,.06)]"
        ),
        # Accent color option.
        "dropdown-accent": (
            "w-[100%] px-3 py-2 "
            "rounded-md border-0 "
            "bg-[transparent] text-[#2563eb] "
            "hover:bg-[rgba(37,99,235,.08)]"
        ),
        # Destructive row.
        "dropdown-danger": (
            "w-[100%] px-3 py-2 "
            "rounded-md border-0 "
            "bg-[transparent] text-[rgb(239,68,68)] "
            "hover:bg-[rgba(239,68,68,.08)]"
        ),
        # Ultra-plain, square edges.
        "dropdown-plain": (
            "w-[100%] px-3 py-2 "
            "rounded-none border-0 "
            "bg-[transparent] text-body "
            "hover:bg-[rgba(15,23,42,.04)]"
        ),
    }

    # ---------- Sizes (applied on top of the variant) ----------
    SIZES = {
        "sm": "text-[12px]",
        "md": "text-[14px]",
        "lg": "text-[16px]",
    }

    # ---------- Optional tones (merged last if provided) ----------
    TONES = {
        "muted":   "text-[rgb(100,116,139)]",
        "primary": "text-[#2563eb]",
        "danger":  "text-[rgb(239,68,68)]",
    }

    # ---------- Defaults ----------
    DEFAULTS = {
        "variant": "sidebar-default",
        "size": "md",
        "tone": "",
    }

    def __init__(
        self,
        *,
        children: str | None = None,
        tag: str = "div",
        variant: str | None = None,
        size: str | None = None,
        tone: str | None = None,
        dzn: str | None = None,   # raw utility escape hatch, merged last
        **attrs,
    ):
        extra_dzn = dzn or attrs.pop("dzn", None)

        # Keep minimal a11y defaults; no JS behaviors for now.
        attrs.setdefault("role", "button")
        attrs.setdefault("tabindex", "0")

        effective_dzn = self._resolve_variant_dzn(
            variant=variant,
            size=size,
            tone=tone,
            extra_dzn=extra_dzn,
        )

        super().__init__(children=children or "", tag=tag, dzn=effective_dzn, **attrs)

    def context(self) -> dict:
        return {}
