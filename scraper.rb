require 'rubygems'
require 'nokogiri'
require 'open-uri'
require "yaml"
require "enumerator"

# http://deposits.parliament.uk/

doc = Nokogiri::HTML(open("deposits.html"))
targets = Array.new

doc.css('tr').each do |tr|
  targets << tr
end

targets.slice!(0..4)
targets.each_slice(4) {|a| 
  b = a.slice!(1..2)
  if b[0] then
  b[0].css('td').each do |td|
    p td.inner_html
  end
end
  p b[1].content if b[1]
  p ""
  }
