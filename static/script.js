function getBody(content)
{
   var x = content.indexOf("<body");
   x = content.indexOf(">", x);
   var y = content.lastIndexOf("</body>");
   return content.slice(x + 1, y);
}

function getContent(content, target)
{
   target.innerHTML =  getBody(content);
}
