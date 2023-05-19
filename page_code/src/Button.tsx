import React from "react";

interface Props {
  border: string;
  color: string;
  children?: React.ReactNode;
  height: string;
  onClick: () => void;
  width: string;
}


const Button: React.FC<Props> = ({
  border,
  color,
  children,
  height,
  onClick,
  width
}) => {
  return (
    <button
      onClick={onClick}
      style={{
        backgroundColor: color,
        border,
        width,
        height,
        borderRadius: 0, 
      }}
    >
      {children}
    </button>
  );
};
export default Button;
