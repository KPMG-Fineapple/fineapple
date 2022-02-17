import Image from "next/image";

export const ItemImage = (props) => {
  const { path, width, height } = props;
  return (
    <>
      <Image
        className="image-wrapper"
        src={path}
        alt="item"
        width={width}
        height={height}
      />
      <style jsx global>{`
        .image-wrapper {
          box-sizing: content-box;
          border-radius: 30px;
        }
      `}</style>
    </>
  );
};
