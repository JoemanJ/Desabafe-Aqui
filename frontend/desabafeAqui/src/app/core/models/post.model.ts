export interface PostModel{
    text: string;
    slug: string;
    created_at: string;
    likes_count: number;
    is_liked: boolean;
    author_details: {
        username: string;
        picture: string;
    }
}

export interface PostCreationModel{
    text: string
}