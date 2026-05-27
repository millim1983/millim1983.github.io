source "https://rubygems.org"

# GitHub Pages 호환 (Pages가 빌드해주므로 로컬도 동일 버전으로 맞춤)
gem "github-pages", group: :jekyll_plugins
gem "minima", "~> 2.5"

# 플랫폼별 의존성
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Ruby 3.x 호환
gem "webrick", "~> 1.7"
