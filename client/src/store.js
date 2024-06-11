import { createStore } from "vuex";
import Cookies from "js-cookie";
import axiosInstance from "./axios-instance";

export default createStore({
  state: {
    userData: null,
  },
  mutations: {
    setUserData(state, userData) {
      state.userData = userData;
    },
    clearUserData(state) {
      state.userData = null;
    },
  },
  actions: {
    async fetchUserData(context) {
      const userId = Cookies.get("user_id");

      if (userId) {
        try {
          const response = await axiosInstance.get(
            "/api/users/getUserByGoogleId",
            {
              params: { googleId: userId },
            }
          );
          context.commit("setUserData", response.data);
        } catch (error) {
          if (error.message && error.response.status === 404) {
            console.log("User not found");
          } else {
            console.error("Error fetching user data:", error);
          }
        }
        // await fetch(
        //   `${process.env.VUE_APP_URL}/api/users/getUserByGoogleId?googleId=${userId}`,
        //   {
        //     method: "GET",
        //   }
        // )
        //   .then((response) => {
        //     if (!response.ok && response.status !== 404) {
        //       throw new Error("Failed to fetch user data");
        //     }
        //     return response.json();
        //   })
        //   .then((data) => {
        //     context.commit("setUserData", data);
        //   })
        //   .catch((error) => {
        //     console.error("Error fetching user data:", error);
        //   });
      }
    },
    // createAndLoginUser(context, { userId, googleData }) {
    //   fetch(
    //     `${process.env.VUE_APP_URL}/api/users/getUserByGoogleId?googleId=${userId}`,
    //     {
    //       method: "GET",
    //     }
    //   )
    //     .then(async (response) => {
    //       if (response.status === 404) {
    //         const user = {
    //           displayName: googleData.name,
    //           googleId: googleData.sub,
    //           profilePicture: googleData.picture,
    //           email: googleData.email,
    //           receiveEmails: true,
    //           role: "registered",
    //         };

    //         const userResponse = await fetch(
    //           `${process.env.VUE_APP_URL}/api/users/createOrUpdateUser`,
    //           {
    //             method: "POST",
    //             headers: {
    //               "Content-Type": "application/json",
    //             },
    //             body: JSON.stringify(user),
    //           }
    //         );

    //         if (!userResponse.ok) {
    //           throw new Error("Failed to create or update user");
    //         }

    //         return userResponse.json();
    //       } else if (!response.ok) {
    //         throw new Error("Failed to fetch user data");
    //       }

    //       return response.json();
    //     })
    //     .then((data) => {
    //       context.commit("setUserData", data);
    //     })
    //     .catch((error) => {
    //       console.error("Error fetching user data:", error);
    //     });
    // },
    async createAndLoginUser(context, { userId, googleData }) {
      try {
        // First request to get user by Google ID
        let response = await axiosInstance.get("/api/users/getUserByGoogleId", {
          params: { googleId: userId },
        });

        // If user is not found, create or update the user
        if (response.status === 404) {
          const user = {
            displayName: googleData.name,
            googleId: googleData.sub,
            profilePicture: googleData.picture,
            email: googleData.email,
            receiveEmails: true,
            role: "registered",
          };

          response = await axiosInstance.post(
            "/api/users/createOrUpdateUser",
            user
          );

          if (!response.data) {
            throw new Error("Failed to create or update user");
          }
        } else if (!response.data) {
          throw new Error("Failed to fetch user data");
        }

        // Commit the user data to the store
        context.commit("setUserData", response.data);
      } catch (error) {
        console.error("Error fetching or creating user data:", error);
      }
    },
    logoutUser(context) {
      context.commit("clearUserData");
    },
  },
  getters: {
    userData: (state) => state.userData,
  },
});
