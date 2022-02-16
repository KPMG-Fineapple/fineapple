const { useRouter } = require("next/router");
const { Layout } = require("src/components/home/layout");

function Item({ item }) {
  const router = useRouter();

  return <>Heello</>;
}

Item.getLayout = (page) => <Layout>{page}</Layout>;

export default Item;

export async function getServerSideProps({ params: { itemId } }) {
  const item = await (
    await fetch(`http://localhost:3001/api/invest/items/${itemId}`)
  ).json();

  return {
    props: {
      item,
    },
  };
}
