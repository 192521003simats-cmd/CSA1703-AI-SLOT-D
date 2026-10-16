# EXPERIMENT 31: CREATE A WEB BLOG USING WORDPRESS

## AIM
To create a web blog using WordPress demonstrating Title tags (`<title>`), Heading tags (`<h1>`-`<h6>`), and Anchor tags (`<a>`).

## WORDPRESS PROCEDURE (5 SIMPLE STEPS)
1. **Login**: Open browser and go to WordPress Admin (`http://localhost/wordpress/wp-admin`).
2. **Set Site Title**: Go to **Settings -> General**, enter Site Title & Tagline, and click **Save Changes**.
3. **Add New Post**: Click **Posts -> Add New**, enter Post Title (generates `<h1>` & `<title>`).
4. **Add Headings & Internal Link**:
   - Add **Heading (H2)** block, set HTML Anchor to `overview` in Block settings.
   - Insert text link pointing to `#overview` to jump internally.
5. **Add External Link**: Highlight text, click Link icon (`Ctrl+K`), enter `https://python.org`, check "Open in new tab", and click **Publish**.

## HTML CODE EQUIVALENT (`web/index.html`)
```html
<!DOCTYPE html>
<html>
<head><title>AI Lab Blog</title></head>
<body>
  <h1>AI Blog</h1>
  <a href="#sec1">Jump to Sec 1</a>
  <h2 id="sec1">Section 1</h2>
  <a href="https://python.org" target="_blank">Python</a>
</body>
</html>
```

## RESULT
Successfully created a WordPress web blog demonstrating Title tags, Heading tags, and Anchor tags.
