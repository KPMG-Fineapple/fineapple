import React from "react";
import { Box, ImageList, ImageListItem } from "@mui/material";
import Typography from "@mui/material/Typography";
import { DashboardLayout } from "../../components/dashboard-layout";
import { useState } from "react";
import { useRouter } from "next/router";

function investDashboard() {
  const router = useRouter();

  return (
    <Box
      sx={{
        marginTop: 30,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <Typography component="h1" variant="h5">
        관심 있으신 투자처를 선택해주세요
      </Typography>
      <ImageList sx={{ display: "flex", padding: 5 }} gap={10}>
        {itemData.map((item, key) => (
          <ImageListItem key={item.img}>
            <img
              src={`${item.img}?w=164&h=164&fit=crop&auto=format`}
              srcSet={`${item.img}?w=164&h=164&fit=crop&auto=format&dpr=2 2x`}
              alt={item.title}
              loading="lazy"
              onClick={() =>
                router.push(`/invest/items/item${Math.floor(key / 2) + 1}`)
              }
            />
          </ImageListItem>
        ))}
      </ImageList>
    </Box>
  );
}

const itemData = [
  {
    img: "https://images.unsplash.com/photo-1551963831-b3b1ca40c98e",
    title: "Breakfast",
  },
  {
    img: "https://images.unsplash.com/photo-1551782450-a2132b4ba21d",
    title: "Burger",
  },
  {
    img: "https://images.unsplash.com/photo-1522770179533-24471fcdba45",
    title: "Camera",
  },
  {
    img: "https://images.unsplash.com/photo-1444418776041-9c7e33cc5a9c",
    title: "Coffee",
  },
  {
    img: "https://images.unsplash.com/photo-1533827432537-70133748f5c8",
    title: "Hats",
  },
  {
    img: "https://images.unsplash.com/photo-1558642452-9d2a7deb7f62",
    title: "Honey",
  },
];

investDashboard.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default investDashboard;
