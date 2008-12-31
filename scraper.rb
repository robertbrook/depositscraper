require 'rubygems'
require 'nokogiri'
require 'open-uri'
require "yaml"
require "enumerator"

# http://deposits.parliament.uk/

doc = Nokogiri::HTML(open("deposits.html"))
targets = Array.new

(doc/"tr").each do |tr|
  targets << tr.inner_html
end

targets.slice!(0..4)
targets.each_slice(4) {|a| y a}


# 
# targets.each_slice(5) {|a| p a}
