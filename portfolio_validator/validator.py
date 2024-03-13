def validate_portfolio(html_content, css_content):
    errors = []

    # Check for welcome section
    if '<section id="welcome-section"' not in html_content:
        errors.append("Your portfolio should have a 'Welcome' section with an id of welcome-section.")

    # Check for h1 element in welcome section
    if '<h1>' not in html_content or '</h1>' not in html_content:
        errors.append("Your #welcome-section element should contain an h1 element.")

    # Check for empty h1 element in welcome section
    if '<h1></h1>' in html_content:
        errors.append("You should not have any empty h1 elements within #welcome-section element.")

    # Check for projects section
    if '<section id="projects"' not in html_content:
        errors.append("You should have a 'Projects' section with an id of projects.")

    # Check for project tile
    if ('<div class="project-title">' not in html_content) and ('<p class="project-title">' not in html_content):
        errors.append("Your portfolio should contain at least one element with a class of project-title.")

    # Check for link in projects section
    if '<a ' not in html_content or 'projects' not in html_content:
        errors.append("Your #projects element should contain at least one a element.")

    # Check for navbar
    if '<nav id="navbar"' not in html_content:
        errors.append("Your portfolio should have a navbar with an id of navbar.")

    # Check for link in navbar
    if '<a ' not in html_content or 'navbar' not in html_content:
        errors.append("Your #navbar element should contain at least one a element whose href attribute starts with #.")

    # Check for profile-link
    if 'id="profile-link"' not in html_content:
        errors.append("Your portfolio should have an a element with an id of profile-link.")

    # Check for target attribute in profile-link
    if 'target="_blank"' not in html_content:
        errors.append("Your #profile-link element should have a target attribute of _blank.")

    # Check for media query
    if '@media' not in css_content:
        errors.append("Your portfolio should use at least one media query.")

    # Check for navbar position
    if 'position: fixed' not in css_content:
        errors.append("Your #navbar element should always be at the top of the viewport.")

    return errors
