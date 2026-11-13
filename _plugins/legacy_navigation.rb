# Preserve old hash-based bookmarks without overriding a remote-theme layout.
Jekyll::Hooks.register :pages, :post_render do |page|
  next unless ['/', '/404.html'].include?(page.url)

  script = '<script src="/assets/js/legacy-navigation.js"></script>'
  page.output = page.output.sub('</head>', "#{script}\n</head>")
end
