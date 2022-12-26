<%
    rows = attr_args
%>
class ${model_name}(db.Model):
    __tablename__ = '${tablename}'
    ${attr_name} = db.Column(db.${attr_type}, 
    % for row in rows:
        ${row},
    % endfor
    )
