import { Container, createTheme, CssBaseline } from "@mui/material";
import Grid from "@mui/material/Grid";
import { useRouter } from "next/router";
import Header from "src/components/home/header";
import MainFeaturedPost from "src/components/home/main-post";
import FeaturedPost from "src/components/home/feature-post";
import { ThemeProvider } from "@mui/styles";

function Main() {
  const router = useRouter();
  const theme = createTheme();

  const mainFeaturedPost = {
    title: "Fine apple의 태양광 솔루션",
    description:
      "소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요",
    image:
      "https://newsimg-hams.hankookilbo.com/2022/02/03/4b4eff73-5adb-40a2-99a3-bf4aa929fa3e.jpg",
    imageText: "main image description",
  };

  const featuredPosts = [
    {
      title: "태양광 올인원 서비스",
      description:
        "소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요",
      image:
        "http://www.solartodaymag.com/news/photo/201706/4574_3285_4224.jpg",
      imageText: "Image Text",
      url: "/home/main",
    },
    {
      title: "태양광 투자 서비스",
      description:
        "소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요 소개문구 써주세요",
      image:
        "https://img.etoday.co.kr/pto_db/2019/01/600/20190121101335_1293391_1200_800.jpg",
      imageText: "Image Text",
      url: "/home/main",
    },
  ];
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg">
        <Header title="Fine apple" sections={[]} />
        <MainFeaturedPost post={mainFeaturedPost} />
        <Grid container spacing={4}>
          {featuredPosts.map((post) => (
            <FeaturedPost key={post.title} post={post} />
          ))}
        </Grid>
      </Container>
    </ThemeProvider>
  );
}

export default Main;
