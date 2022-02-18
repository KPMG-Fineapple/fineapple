import { Box, ImageList, ImageListItem, Grid } from "@mui/material";
import Typography from "@mui/material/Typography";
import { useRouter } from "next/router";
import { Layout } from "src/components/home/layout";
import Card from "src/components/invest/card";

function investDashboard() {
  const router = useRouter();

  return (
    <Layout>
      <Box
        sx={{
          marginTop: 10,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Box sx={{ marginBottom: 8 }}>
          <Typography component="h1" variant="h4">
            관심 있는 발전소를 선택해주세요
          </Typography>
        </Box>

        <Grid container spacing={3} columns={27} sx={{ maxWidth: 3000 }}>
          {itemData.map((item, key) => (
            <Grid item xs={9}>
              <Card
                imgURL={`/static/images/items/item${item.num}`}
                srcSet={`${item.img}?w=164&h=164&fit=crop&auto=format&dpr=2 2x`}
                alt={item.title}
                num={item.num}
              />
            </Grid>
          ))}
        </Grid>
      </Box>
    </Layout>
  );
}

const itemData = [
  {
    img: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Photovoltaik_Dachanlage_Hannover_-_Schwarze_Heide_-_1_MW.jpg/220px-Photovoltaik_Dachanlage_Hannover_-_Schwarze_Heide_-_1_MW.jpg",
    title: "Breakfast",
    num: 1,
  },
  {
    img: "https://atmosphere.copernicus.eu/sites/default/files/inline-images/solarpanels_small.png",
    title: "Burger",
    num: 2,
  },
  {
    img: "https://idsb.tmgrup.com.tr/ly/uploads/images/2022/01/11/thumbs/800x531/174025.jpg?v=1641907676",
    title: "Camera",
    num: 3,
  },
  {
    img: "https://imageio.forbes.com/specials-images/imageserve/604a84cb9488bb7a177e67ba/Aerial-View-Of-Solar-Panels-On-Tree/960x0.jpg?fit=bounds&format=jpg&width=960",
    title: "Coffee",
    num: 4,
  },
  {
    img: "https://d12oja0ew7x0i8.cloudfront.net/image-handler/ts/20211123093933/ri/750/src/images/news/ImageForNews_57421_16376783723446339.jpg",
    title: "Hats",
    num: 5,
  },
  {
    img: "https://www.sciencenewsforstudents.org/wp-content/uploads/2020/10/1030_LL_solar_power-1028x579.jpg",
    title: "Honey",
    num: 6,
  },
];

export default investDashboard;
