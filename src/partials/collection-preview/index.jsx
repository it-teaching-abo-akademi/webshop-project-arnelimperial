import React from "react";

const CollectionPreview = ({ title, routeName, items }) => (
  <div>
    <h1>{title.toUpperCase()}</h1>
    <p>{routeName}</p>

    <div>
      {items
        .filter((item, idx) => idx < 4)
        .map((item) => (
          <div key={item.id}>
            {item.name}
           
          </div>
        ))}
    </div>
  </div>
);

export default CollectionPreview;
