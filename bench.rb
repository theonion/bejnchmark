types = ['templatetags', 'includes']
steps = [1, 10, 100, 1_000, 10_000, 100_000]
for type in types
  for depth in [1]
    for count in steps
      if depth * count <= 100_000
        start = Time.now
        `curl -s http://localhost:8000/#{type}/#{depth}/#{count} > /dev/null`
        duration = Time.now - start
        puts %|=SPLIT("#{[type, depth, count, duration, depth * count] * ', '}", ",")|
      end
    end
  end
end
