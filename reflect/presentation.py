from website.common import create_menu_content

MENU = [
    [
        "Project",
        [
            [
                "Why Reflect?",
                "context.md",
            ],
            ["Who are we?", "information/team.md"],
            ["Become a Teky", "information/community.md"],
            ["Targeted users", "information/targeted_users.md"],
            # ["Investors", "information/investors.md"],
            ["Feedback", "information/feedback.md"],
        ],
    ],
    [
        "Alternatives",
        [
            ["Scientific", "scientific_frameworks.md"],
            ["Commercial", "commercial_frameworks.md"],
        ],
    ],
]


def content(module_argument):
    return create_menu_content(
        MENU,
        "reflect.md",
        overview_name="What is Reflect?",
        folder="website/reflect",
        module_argument=module_argument,
    )
